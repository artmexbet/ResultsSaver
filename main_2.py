from copy import deepcopy
from flask import Flask, request, jsonify
from Utilities import *
from datetime import datetime

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


def new_db(data: dict):  # по поводу этой штуки вообще не уверен
    global subjects, d
    if data["is_admin"]:
        subjects = JsonDB(f"subjects-{datetime.now().date()}.json", {})
        d = Day(str(datetime.now().date()) + ".json", subjects)
        return "0"
    return "-1"


subjects = JsonDB("subjects.json")
d = Day("test1.json", subjects)
admins = JsonDB("admins.json", {})


@app.route("/")
def main():
    return "Это backend часть этого сайта"


@app.route("/users", methods=["GET", "POST"])
def users():
    """
    При POST запросе этот route запишет в бд людей,
    При GET запросе вернёт json файл с всеми пользователями
    :return: JSON с пользователями; 0; error
    """
    if request.method == "GET":
        return jsonify(d)
    else:
        data = request.data
        xlsx_file = save_xlsx_file(str(datetime.now().date()) + ".xlsx", data)
        json_from_xlsx(xlsx_file, d)
        return {"verdict": "ok"}, 200


@app.route("/users_sum")
def all_sum():
    result = {'users': deepcopy(d['users'])}
    for i in result['users']:
        i['result'] = sum([int(k[1]) for j in i['days'] for k in j.values()])
        del i['days']
    return jsonify(result), 200


@app.route("/add_result/<int:user_id>", methods=["POST"])
def add_result(user_id):
    """
    Здесь добавляем результаты людям
    :param user_id: id пользователя, которому будут добавлены баллы
    :return: Прога вернёт вердикт, в нормальном положении это что-то вроде "ok"
    """
    # Пример запроса в файле result_example.json
    data = request.get_json()
    return d.add_result(user_id, data["subject"], data["score"])


@app.route("/test_for_correct", methods=["POST"])
def search():
    data = request.get_json()
    """Пример json в файле example.json"""
    if not any(map(lambda x: x == data['id'], d["users"])):
        return "3"  # Ошибка идентификатора
    elif data["subject"] not in subjects.keys():
        return "1"  # Такого предмета не существует
    elif data["score"] not in range(subjects[data["subject"]][1] + 1):
        return "4"  # Невозможные баллы
    else:
        return "0"  # Всё прошло успешно


@app.route("/recount", methods=["POST"])
def recount_main():
    # Пример запроса смотрите в файле recount_example.json
    data = request.get_json()
    if data["is_admin"]:
        recount(d, subjects)
        return "0"
    return "-1"


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    d["users"].append(data)
    sorting(d)
    return "0"


@app.route("/check_admins", methods=["POST"])
def check_admins():
    data = request.get_json()
    if any(map(lambda x: x["login"] == data["login"] and x["password"] == data["password"], admins["admins"])):
        return {"data": {"access": True}}
    return {"data": {"access": False}}


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
        return "0"
    return "-1"


@app.route("/remove_admin", methods=['POST'])
def remove_admin():
    data = request.get_json()
    try:
        for i, elem in enumerate(admins["admins"]):
            if elem["login"] == data["login"]:
                break
        admins["admins"].remove(i)
        admins.commit()
    except Exception as ex:
        return str(ex)


@app.route("/add_subject", methods=["POST"])
def add_subject():
    data = request.get_json()
    if data["subject"] not in subjects.keys():
        subjects[data["subject"]] = data["values"]
        return {"status": 0}
    return {"status": -1}


if __name__ == '__main__':
    app.run(host="192.168.1.85", port=5050)
