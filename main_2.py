from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

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
        # Тут мы будем добавлять в базу данных людей, если их там нет
        pass


@app.route("/add_result/<subject>/<int:user_id>", methods=["POST"])
def add_result(subject: str, user_id: int):
    """
    Здесь добавляем результаты людям
    :param subject: Имя предмета, по которому мы будем добавлять результаты
    :param user_id: id пользователя, которому будут добавлены баллы
    :return: Прога вернёт вердикт, в нормальном положении это что-то вроде "ok"
    """
    pass


if __name__ == '__main__':
    app.run()
