from flask import Flask, render_template, request, redirect
from Utilities import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///table.db'
db = SQLAlchemy(app)


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


if __name__ == '__main__':
    app.run()
