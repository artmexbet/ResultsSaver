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
    :return: JSON с пользователями; ok; error
    """
    if request.method == "GET":
        return {"id": ["params"]}
    else:
        data = request.data
        xlsx_file = save_xlsx_file(str(datetime.now().date()), data)
        return "ok"


@app.route("/add_result/<int:user_id>", methods=["POST"])
def add_result(user_id: int):
    """
    Здесь добавляем результаты людям
    :param user_id: id пользователя, которому будут добавлены баллы
    :return: Прога вернёт вердикт, в нормальном положении это что-то вроде "ok"
    """
    pass


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


if __name__ == '__main__':
    app.run()
