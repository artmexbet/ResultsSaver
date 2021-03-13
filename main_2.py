from flask import Flask, request
from Utilities import *
from datetime import datetime

app = Flask(__name__)
subjects = JsonDB("subjects.json")
d = Day("test.json", subjects)


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
        return d
    else:
        data = request.data
        xlsx_file = save_xlsx_file(str(datetime.now().date()) + ".xlsx", data)
        return 0


@app.route("/add_result/<user_id>", methods=["POST"])
def add_result(user_id):
    """
    Здесь добавляем результаты людям
    :param user_id: id пользователя, которому будут добавлены баллы
    :return: Прога вернёт вердикт, в нормальном положении это что-то вроде "ok"
    """
    # Пример запроса в файле result_example.json
    data = request.json
    return d.add_result(user_id, data["subject"], data["score"])


@app.route("/test_for_correct", methods=["POST"])
def search():
    data = request.json
    """Пример json в файле example.json"""
    if data["id"] not in d.keys():
        return 3  # Ошибка идентификатора
    elif data["subject"] not in subjects.keys():
        return 1  # Такого предмета не существует
    elif data["score"] not in range(subjects[data["subject"]][1] + 1):
        return 4  # Невозможные баллы
    else:
        return 0  # Всё прошло успешно


@app.route("/create_new_db", methods=["POST"])
def new_db():  # по поводу этой штуки вообще не уверен
    global subjects, d
    data = request.json
    subjects = JsonDB(f"subjects-{datetime.now().date()}.json")
    d = Day(str(datetime.now().date()) + ".json", subjects)
    return 0


@app.route("/recount", methods=["POST"])
def recount_main():
    # Пример запроса смотрите в файле recount_example.json
    data = request.json
    if data["is_admin"]:
        pass


if __name__ == '__main__':
    app.run(debug=True)
