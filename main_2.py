from copy import deepcopy
from flask import Flask, request, jsonify
from Utilities import *
from datetime import datetime
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
cors = CORS(app)


def new_db(data: dict):  # по поводу этой штуки вообще не уверен
    global subjects, d
    if data["is_admin"]:
        subjects = JsonDB(f"subjects-{datetime.now().date()}.json", {})
        d = Day(str(datetime.now().date()) + ".json", subjects)
        return {"verdict": "ok"}, 200
    return {"error": "You aren't admin"}, 401


subjects = JsonDB("subjects.json")
d = Day("test1.json", subjects)
admins = JsonDB("admins.json", {})


@app.route("/")
@cross_origin()
def main():
    return "Это backend часть этого сайта"


@app.route("/users", methods=["POST"])
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


@app.route("/users/<int:day>")
def users_per_day(day):
    temp_data = Day("test1.json", subjects)
    try:
        for i in range(len(temp_data["users"])):
            try:
                temp_data["users"][i]["results"] = temp_data["users"][i]["days"][day]
            except IndexError:
                temp_data["users"][i]["results"] = []
            del temp_data["users"][i]["days"]
        return temp_data
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


@app.route("/replace_results", methods=["PUT"])
def replace_results():
    global d
    data = request.get_json()
    if data["is_admin"]:
        del data["is_admin"]
        d = Day(d.directory.split("/")[1], subjects, data)
        return {"verdict": "ok"}, 200
    return {"error": "You haven't admin's roots"}, 401


@app.route("/users/<int:id>", methods=["PATCH"])
def patch_results(id):
    item = d.find_item_with_id(id)
    not_valid = []
    if item:
        data = request.get_json()
        for i in data.items():
            if i[0] in item.keys():
                item[i[0]] = i[1]
            else:
                not_valid.append(i)
        if not_valid:
            return {"error": {"not_valid": not_valid}}, 400
        else:
            return {"verdict": "ok"}, 200
    else:
        return {"error": "No such id in database"}, 404


@app.route("/users_sum")
def all_sum():
    result = {'users': deepcopy(d['users'])}
    for i in result['users']:
        i['result'] = student_sum(i)
        del i['days']
    return result, 200


@app.route("/add_result/<int:user_id>", methods=["POST"])
def add_result(user_id):
    """
    Здесь добавляем результаты людям
    :param user_id: id пользователя, которому будут добавлены баллы
    :return: Прога вернёт вердикт, в нормальном положении это что-то вроде "ok"
    """
    # Пример запроса в файле add_result.json
    data = request.get_json()
    if data["is_admin"]:
        data = data["data"]
        student = d.find_item_with_id(user_id)
        if student["class"] == data["class"] and subjects[data["subject"]][2] == student["class"]:
            return d.add_result(user_id, data["subject"], data["score"]), 200
    return {"error": "You aren't admin!"}, 401


@app.route("/test_for_correct", methods=["POST"])
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


@app.route("/recount", methods=["POST"])
def recount_main():
    # Пример запроса смотрите в файле recount_example.json
    data = request.get_json()
    if data["is_admin"]:
        recount(d, subjects)
        return {"verdict": "ok"}, 200
    return {"error": "You aren't admin"}, 401


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    d["users"].append(data)
    sorting(d)
    return {"verdict": "ok"}, 200


@app.route("/check_admins", methods=["POST"])
def check_admins():
    data = request.get_json()
    try:
        if any(map(lambda x: x["login"] == data["login"] and x["password"] == data["password"], admins["data"])):
            return {"data": {"access": 1, "speciality": admins.get_from_key("subject")}}, 200
        return {"data": {"access": 0}}, 200
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


@app.route("/new_db", methods=["POST"])
def route_new_db():
    new_db(request.get_json())


@app.route("/add_admin", methods=["POST"])
def add_admin():
    data = request.get_json()
    if data["is_admin"]:
        data.pop("is_admin")
        admins["admins"].append(data)
        admins.commit()
        return {"verdict": "ok"}, 200
    return {"error": "You aren't admin"}, 401


@app.route("/remove_admin", methods=['POST'])
def remove_admin():
    data = request.get_json()
    try:
        for i, elem in enumerate(admins["admins"]):
            if elem["login"] == data["login"]:
                break
        admins["admins"].remove(i)
        admins.commit()
        return {"verdict": "ok"}, 200
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


@app.route("/add_subject", methods=["POST"])
def add_subject():
    data = request.get_json()
    if data["subject"] not in subjects.keys():
        subjects[data["subject"]] = data["values"]
        return {"verdict": "ok"}, 200
    return {"error": "BadRequest"}, 400


@app.route("/users/betters/<class_dig>")
def betters_students_from_class(class_dig):
    if class_dig not in range(5, 10) and not isinstance(class_dig, int):
        return {"error": "BadRequest"}, 400
    all_this_class_students = d.find_item_with_class(class_dig)
    return {"data": sorted(all_this_class_students, key=lambda x: student_sum(x))}, 200


@app.route("/users/betters/<subject>")
def betters_student_from_subject(subject):
    if not isinstance(subject, str) and subject not in subjects.keys():
        return {"error": "BadRequest"}, 400
    all_this_subject_students = d.find_item_with_subjects(subject)
    return {"data": sorted(all_this_subject_students, key=lambda x: student_sum(x))}, 200


@app.route("/subjects")
def get_subjects():
    return subjects, 200


@app.route("/delete_user", methods=["DELETE"])
def delete_user():
    data = request.get_json()
    try:
        if data["is_admin"]:
            data = data["data"]
            a = d.find_item_with_id(data["id"])
            del a
            return {"verdict": "ok"}, 200
        return {"error": "You aren't admin"}, 401
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


if __name__ == '__main__':
    app.run(host="192.168.1.85", port=5050)
