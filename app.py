from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///table.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(300), nullable=False, primary_key=True)
    password = db.Column(db.String(300), nullable=False)
    name = db.Column(db.String(300), nullable=False)
    class_digit = db.Column(db.Integer, nullable=False)
    stage = db.Column(db.String(4), nullable=False)
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
        data = request.form
        if data["Password"] != data["Password_confirmation"]:
            return render_template("reg.html", is_password_possible=False, is_form_passed=True)
        if not all(data.values()):
            return render_template("reg.html", is_all_fields_filled=False, is_form_passed=True)
        user = User(name=f'{data["Name"]} {data["Surname"]} {data["Lastname"]}', class_digit=int(data["Stage_number"]),
                    stage=data["Stage_letter"], is_command=(1 if data["Teamed"] == "on" else 0), login=data['Login'],
                    password=data['Password'])

        db.session.add(user)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("reg.html", is_form_passed=False)


@app.route("/")
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run()
