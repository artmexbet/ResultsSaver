from copy import deepcopy
from flask import Flask, request, jsonify, render_template
from Utilities import *
from datetime import datetime
from flask_cors import CORS, cross_origin
from waitress import serve

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
cors = CORS(app)
config = Config()


def new_db(data: dict):  # по поводу этой штуки вообще не уверен
    global subjects, d
    subjects_name = f"subjects-{datetime.now().date()}.json"
    subjects = JsonDB(subjects_name, {})
    day_name = str(datetime.now().date()) + ".json"
    d = Day(day_name, subjects)
    config.set_configs(current_students=day_name, current_subjects=subjects_name)
    return {"verdict": "ok"}, 200


subjects = JsonDB(config.current_subjects)
d = Day(config.current_students, subjects)
d.set_day(new_day=config.day)
admins = JsonDB(config.current_admins, {})


def users_per_day(day):
    temp_data = Day("test1.json", subjects)
    try:
        for i in range(len(temp_data["users"])):
            try:
                temp_data["users"][i]["results"] = temp_data["users"][i]["days"][day]
            except IndexError:
                temp_data["users"][i]["results"] = {}
            del temp_data["users"][i]["days"]
        return temp_data['users']
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


@app.route("/")
@cross_origin()
def main():
    return render_template("main.html", day=1, users=users_per_day(0))


@app.route("/<int:day>")
def main_2(day):
    return render_template("main.html", day=day + 1, users=users_per_day(day))


@app.route("/users", methods=["POST"])
@cross_origin()
def users():
    """
    Этот route записывает в бд людей
    :return: JSON с пользователями; 0; error
    """
    data = request.data
    xlsx_file = save_xlsx_file(str(datetime.now().date()) + ".xlsx", data)
    json_from_xlsx(xlsx_file, d)
    # sorting(d)
    return {"verdict": "ok"}, 200


@app.route("/users/<int:day>/<int:user_id>")
@cross_origin()
def get_user(day, user_id):
    try:
        user = d.get_item_with_id(user_id).copy()
        temp_result = [{"subject": key, "value": value[1]} for key, value in user["days"][day].items()]
        user["results"] = temp_result
        user.pop("days")
        return render_template("more.html", user=user)
    except Exception as ex:
        print(ex)
        return {"error": "Такого пользователя не существует"}, 404


@app.route("/replace_results", methods=["PUT"])
@cross_origin()
def replace_results():
    global d
    data = request.get_json()
    d = Day(d.directory.split("/")[1], subjects, data)
    return {"verdict": "ok"}, 200


@app.route("/users/<int:id>", methods=["PATCH"])
@cross_origin()
def patch_users(id):
    item = d.get_item_with_id(id)
    not_valid = []
    if item:
        data = request.get_json()
        for i in data.items():
            if i[0] in item.keys():
                item[i[0]] = i[1]
            else:
                not_valid.append(i)
        d.commit()
        if not_valid:
            return {"error": {"not_valid": not_valid}}, 400
        else:
            return {"verdict": "ok"}, 200
    else:
        return {"error": "No such id in database"}, 404


@app.route("/users/results/<int:user_id>", methods=["PATCH"])
@cross_origin()
def patch_results(user_id):
    changes = request.get_json()
    student = d.get_item_with_id(user_id)
    for change_key, change_value in changes.items():
        for day_ind in range(len(student["days"])):
            if change_key in student["days"][day_ind].keys():
                student["days"][day_ind][change_key] = change_value
    d.commit()


@app.route("/sum")
@cross_origin()
def all_sum():
    result = {'users': deepcopy(d['users'])}
    for i in result['users']:
        i['result'] = student_sum(i)
        del i['days']
    return result, 200


@app.route("/add_result/<int:user_id>", methods=["POST"])
@cross_origin()
def add_result(user_id):
    """
    Здесь добавляем результаты людям
    :param user_id: id пользователя, которому будут добавлены баллы
    :return: Прога вернёт вердикт, в нормальном положении это что-то вроде "ok"
    """
    # Пример запроса в файле add_result.json
    data = request.get_json()
    try:
        student = d.get_item_with_id(user_id)
        if student["class"] in subjects[data["subject"]][2]:
            return d.add_result(user_id, data["subject"], data["score"], student)
        return {"error": "Этот пользователь не может писать этот предмет"}, 400
    except Exception as ex:
        print(ex)
        return {"error": str(ex)}, 400


@app.route("/test_for_correct", methods=["POST"])
@cross_origin()
def search():
    data = request.get_json()
    """Пример json в файле example.json"""
    if not any(map(lambda x: x == data['id'], d["users"])):
        return {"error": "This id doesn't exist"}, 400  # Ошибка идентификатора
    elif data["subject"] not in subjects.keys():
        return {"error": "This subject doesn't exist"}, 400  # Такого предмета не существует
    elif data["score"] not in range(subjects[data["subject"]][1] + 1):
        return {"error": "Unbelievable score"}, 400  # Невозможные баллы
    else:
        return {"verdict": "ok"}, 200  # Всё прошло успешно


@app.route("/recount", methods=["GET"])
@cross_origin()
def recount_main():
    # Пример запроса смотрите в файле recount_example.json
    recount(d, subjects)
    return {"verdict": "ok"}, 200


@app.route("/add_user", methods=["POST"])
@cross_origin()
def add_user():
    data = request.get_json()
    d.add_user(data)
    return {"verdict": "ok"}, 200


@app.route("/check_admins", methods=["POST"])
@cross_origin()
def check_admins():
    data = request.get_json()
    try:
        if any(map(lambda x: x["login"] == data["login"] and x["password"] == data["password"], admins["data"])):
            return {"data": {"access": 1, "speciality": admins.get_from_key("login", data["login"])["subject"]}}, 200
        return {"data": {"access": 0}}, 200
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


@app.route("/new_db", methods=["POST"])
@cross_origin()
def route_new_db():
    new_db(request.get_json())


@app.route("/add_admin", methods=["POST"])
@cross_origin()
def add_admin():
    data = request.get_json()
    admins["data"].append(data)
    admins.commit()
    return {"verdict": "ok"}, 200


@app.route("/remove_admin", methods=['POST'])
@cross_origin()
def remove_admin():
    data = request.get_json()
    try:
        for i, elem in enumerate(admins["data"]):
            if elem["login"] == data["login"]:
                admins["data"].remove(elem)
                break
        admins.commit()
        return {"verdict": "ok"}, 200
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


@app.route("/add_subject", methods=["POST"])
@cross_origin()
def add_subject():
    data = request.get_json()
    if data["subject"] not in subjects.keys():
        subjects[data["subject"]] = data["values"]
        subjects.commit()
        return {"verdict": "ok"}, 200
    return {"error": "BadRequest"}, 400


@app.route("/users/betters/<int:day>")
@cross_origin()
def betters_students(day):
    if day not in range(2):
        return {"error": "BadRequest"}, 400
    students = sorted(d["users"].copy(), reverse=True,
                      key=lambda x: sum(map(lambda k: k[1],
                                            sorted(x["days"][day].values(), reverse=True, key=lambda j: j[1])[:2])))
    # if class_dig not in range(*d.classes_count) and not isinstance(class_dig, int):
    #     return {"error": "BadRequest"}, 400
    # all_this_class_students = convert_to_betters(d.get_items_with_class(class_dig))
    return render_template("main.html", day=day + 1, users=students[:20])


@app.route("/users/betters/<subject>")
@cross_origin()
def betters_student_from_subject(subject):
    if not isinstance(subject, str) and subject not in subjects.keys():
        return {"error": "BadRequest"}, 400
    all_this_subject_students = d.find_item_with_subjects(subject)
    return {"data": sorted(all_this_subject_students, key=lambda x: -get_subject_result(x, subject))[:20]}, 200


@app.route("/subjects")
@cross_origin()
def get_subjects():
    return {"data": list(subjects.keys())}, 200


@app.route("/delete_user", methods=["DELETE"])
@cross_origin()
def delete_user():
    data = request.get_json()
    try:
        d.remove(d.get_item_with_id(data["id"]))
        return {"verdict": "ok"}, 200
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


@app.route("/change_day", methods=["PUT"])
@cross_origin()
def change_day():
    new_day = request.get_json()["new_day"]
    d.set_day(new_day=new_day)
    config.set_configs(day=new_day)
    return {"verdict": "ok"}, 200


@app.route("/users/betters/<subject>/<int:class_d>")
@cross_origin()
def betters_student_from_subject_n_class(subject, class_d):
    temp = sorted(list(filter(lambda x: x["class"] == class_d, betters_student_from_subject(subject))),
                  key=lambda x: -get_subject_result(x, subject))[:20]
    for user_id in range(len(temp)):
        temp[user_id]["result"] = sum(temp[user_id]["results"].values())
        temp[user_id].pop("results")
    return {"data": temp}, 200


@app.route("/users/betters")
@cross_origin()
def betters():
    return {"data": sorted(convert_to_betters(d["users"])[20:], key=lambda x: -sum(x["results"].values()))}


@app.route("/admins")
@cross_origin()
def get_admins():
    return jsonify(admins), 200


@app.route("/users/betters/teams")
@cross_origin()
def better_teams():
    return {"data": d.count_teams}


@app.route("/login")
def login():
    pass


if __name__ == '__main__':
    app.run(host="localhost")
    # serve(app, host='0.0.0.0', port=8080)
    # serve(app, host="0.0.0.0", port=5000)
