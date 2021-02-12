from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///tables.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    class_digit = db.Column(db.String(4), nullable=False)
    stage = db.Column(db.Integer, nullable=False)
    is_command = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id


class UserResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maths = db.Column(db.Integer, nullable=False, default=0)
    # Дальше живут драконы

    def __repr__(self):
        return "<UserResult %r>" % self.id


@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        pass
    else:
        return render_template("main.html")


@app.route("/")
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run()
