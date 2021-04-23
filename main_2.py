import logging
from datetime import datetime

from flask import Flask, request, render_template, redirect, abort
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from waitress import serve

from Utilities import *
from data import db_session
from data.admins import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["SECRET_KEY"] = "abrakadabra-key"
app.config["UPLOAD_FOLDER"] = "temp_files"
config = Config()
logging.basicConfig(filename='main.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.DEBUG)


@app.errorhandler(500)
def handler_500(error):
    logging.critical("Internal Server Error")
    return "Internal Server Error"


@app.errorhandler(404)
def handler_404(error):
    logging.critical("Not Found")
    return "Not Found"


def new_db():  # по поводу этой штуки вообще не уверен
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
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(admin_id):
    db_sess = db_session.create_session()
    return db_sess.query(Admin).get(admin_id)


def users_per_day(day):
    temp_data = Day("test1.json", subjects)
    try:
        for i in range(len(temp_data["users"])):
            try:
                temp_data["users"][i]["results"] = temp_data["users"][i]["days"][day]
            except IndexError:
                temp_data["users"][i]["results"] = {}
            del temp_data["users"][i]["days"]
        logging.info(f"Info about users in {day} day was received")
        return temp_data['users']
    except Exception as ex:
        print(ex)
        logging.error(f"An error occurred: {ex} \n during received users")
        return {"error": "BadRequest"}, 400


@app.route("/")
def main():
    args = request.args
    data = users_per_day(0)
    data = filtered_data(args, data)
    return render_template("main.html", day=1, users=data, config=config, subjects=list(subjects))


@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == "POST":
        form = request.form
        db_sess = db_session.create_session()
        if db_sess.query(Admin).filter(Admin.email == form["email"]).first():
            return render_template('register.html',
                                   message="Такой пользователь уже есть",
                                   subjects=list(subjects.keys()) + ["Главный админ"])
        user = Admin(
            name=form["name"],
            email=form["email"],
            subject=form["subject"]
        )
        user.set_password(form["password"])
        db_sess.add(user)
        db_sess.commit()
        return redirect('/admins')
    return render_template('register.html', subjects=list(subjects.keys()) + ["Главный админ"])


@app.route("/admins/<int:admin_id>", methods=["GET", "POST"])
@login_required
def update_admins(admin_id):
    sess = db_session.create_session()
    cur_admin = sess.query(Admin).filter(Admin.id == admin_id).first()
    if request.method == "GET":
        return render_template("update_admins.html", admin=cur_admin,
                               subjects=list(subjects.keys()) + ["Главный админ"])
    form = request.form
    cur_admin.name = form.get("name", cur_admin.name)
    cur_admin.subject = form.get("subject", cur_admin.subject)
    sess.commit()
    return redirect("/admins")


@app.route("/<int:day>")
def main_2(day):
    args = request.args
    data = users_per_day(day)
    data = filtered_data(args, data)
    return render_template("main.html", day=day + 1, users=data, config=config,
                           subjects=list(subjects.keys()))


def filtered_data(args, data):
    """
    Функция возвращает отфильтрованные данные
    :param args: ключи фильтрации
    :param data: данные для фильтрации
    :return:
    """
    if args:
        for key, value in args.items():
            if value:
                if key == "subject":
                    data = list(filter(lambda x: value in x["results"].keys(), data))
                elif key == "class":
                    data = list(filter(lambda x: x["class"] == int(value), data))
    return data


@app.route("/users/<int:day>/<int:user_id>", methods=["post", "get"])
def get_user(day, user_id):
    try:
        if request.method == "GET":
            user = d.get_item_with_id(user_id).copy()
            temp_result = [{"subject": key, "value": value} for key, value in user["days"][day].items()]
            user["results"] = temp_result
            user.pop("days")
            logging.info("Info about users was received")
            return render_template("more.html", user=user, config=config.opened_day, day=day)
        data = request.form
        temp = {key[:-6]: value for key, value in data.items()}
        for key, value in data.items():
            temp[key[:-6]] = int(value)
        patch_results(user_id, temp)
        return redirect("/")
    except Exception as ex:
        print(ex)
        logging.error(f"An error occurred: {ex} \n during received users")
        return {"error": "Такого пользователя не существует"}, 404


def patch_users(user_id, data: dict):
    item = d.get_item_with_id(user_id)
    not_valid = []
    if item:
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


def patch_results(user_id, changes: dict):
    # changes = request.get_json()
    student = d.get_item_with_id(user_id)
    for change_key, change_value in changes.items():
        for day_ind in range(len(student["days"])):
            if change_key in student["days"][day_ind].keys():
                student["days"][day_ind][change_key] = [change_value, -1]
    d.commit()


@app.route("/sum")
def all_sum():
    result = {'users': deepcopy(d['users'])}
    for i in result['users']:
        i['result'] = student_sum(i)
        del i['days']
    return result, 200


def add_result(user_id, data):
    """
    Здесь добавляем результаты людям
    :param user_id: id пользователя, которому будут добавлены баллы
    :param data: информация о результате пользователя
    :return: Прога вернёт вердикт, в нормальном положении это что-то вроде "ok"
    """
    try:
        student = d.get_item_with_id(user_id)
        if student["class"] in subjects[data["subject"]][2]:
            return d.add_result(data["subject"], data["score"], student)
        return {"error": "Этот пользователь не может писать этот предмет"}, 401
    except Exception as ex:
        print(ex)
        logging.error(f"An error occurred: {ex} \n during adding some results")
        return {"error": str(ex)}, 400


@app.route("/users/count")
@login_required
def recount_main():
    recount(d, subjects)
    return redirect("/")


def add_user():
    data = request.get_json()
    d.add_user(data)
    return {"verdict": "ok"}, 200


def route_new_db():
    new_db()


@app.route("/admins/<int:admin_id>/delete")
@login_required
def remove_admin(admin_id):
    try:
        sess = db_session.create_session()
        sess.delete(sess.query(Admin).filter(Admin.id == admin_id).first())
        sess.commit()
        return redirect("/admins")
    except Exception as ex:
        print(ex)
        logging.error(f"An error occurred: {ex} \n during admins deleting")
        return {"error": "BadRequest"}, 400


@app.route("/users/betters/<int:day>")
def betters_students(day):
    args = request.args
    if day not in range(2):
        return {"error": "BadRequest"}, 400
    students = sorted(deepcopy(d["users"]), reverse=True,
                      key=lambda x: sum(map(lambda k: k[1],
                                            sorted(x["days"][day].values(), reverse=True, key=lambda j: j[1])[:2])))
    for i, student in enumerate(students):
        students[i]["results"] = student["days"][day]
        students[i].pop("days")
    return render_template("main.html", day=day + 1, users=filtered_data(args, students)[:20], subjects=subjects)


@app.route("/users/betters/<subject>")
def betters_student_from_subject(subject):
    if not isinstance(subject, str) and subject not in subjects.keys():
        return {"error": "BadRequest"}, 400
    all_this_subject_students = d.find_item_with_subjects(subject)
    return {"data": sorted(all_this_subject_students, key=lambda x: -get_subject_result(x, subject))[:20]}, 200


@app.route("/subjects")
def get_subjects():
    return {"data": list(subjects.keys())}, 200


def delete_user():
    data = request.get_json()
    try:
        d.remove(d.get_item_with_id(data["id"]))
        return {"verdict": "ok"}, 200
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


@app.route("/users/betters/<subject>/<int:class_d>")
def betters_student_from_subject_n_class(subject, class_d):
    temp = sorted(list(filter(lambda x: x["class"] == class_d, betters_student_from_subject(subject))),
                  key=lambda x: -get_subject_result(x, subject))[:20]
    for user_id in range(len(temp)):
        temp[user_id]["result"] = sum(temp[user_id]["results"].values())
        temp[user_id].pop("results")
    return {"data": temp}, 200


@app.route("/users/betters")
def betters():
    return {"data": sorted(convert_to_betters(d["users"])[20:], key=lambda x: -sum(x["results"].values()))}


@app.route("/admins")
@login_required
def get_admins():
    sess = db_session.create_session()
    return render_template("admins_list.html", admins=sess.query(Admin).all()), 200


@app.route("/users/betters/teams")
def better_teams():
    return {"data": d.count_teams}


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_page.html")
    form = request.form
    mail = form["email"]
    password = form["password"]
    remember_me = True if form.get("remember_me", False) else False
    db_sess = db_session.create_session()
    user = db_sess.query(Admin).filter(Admin.email == mail).first()
    logging.info(f"{user} was connected to site")
    messages = []
    if user:
        if user.check_password(password):
            login_user(user, remember=remember_me)
            return redirect("/admin")
        messages.append("Неверный")
    else:
        messages.append("Пользователя с таким email не существует!")
    return render_template("login_page.html", message="<br>".join(messages))


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if request.method == "GET":
        return render_template("admin.html", config=config,
                               subjects={subject: [value[0], value[1], ",".join([str(i) for i in value[2]])] for
                                         subject, value in subjects.items()})
    form = request.files
    if "file" not in form.keys():
        return "Нет файла!"
    file = form["file"]
    if file.name == "":
        return redirect("/admin")
    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)
    json_from_xlsx(openpyxl.load_workbook(path), d)
    return redirect("/admin")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/users/results", methods=["GET", "POST"])
@login_required
def res():
    if request.method == "GET":
        return render_template("add_results.html", subjects=list(subjects.keys()))
    form = request.form
    answer = add_result(int(form["id"]),
                        {"subject": form.get("subject", current_user.subject), "score": int(form["score"])})
    if answer[1] == 401:
        return render_template("add_results.html", subjects=list(subjects.keys()),
                               message="Ученик не может писать этот предмет!"
                                       " Возможно, в этот день его ещё не проводили.")
    if answer[1] != 200:
        abort(answer[1])
    else:
        return redirect("/users/results")


@app.route("/users/change-day/<int:day>")
@login_required
def change_day(day):
    if day in range(3):
        if day in range(1, 3):
            d.set_day(new_day=day - 1)
            config.set_configs(day=day - 1)
        config.set_configs(opened_day=day)
        return redirect("/admin")
    else:
        abort(404)


@app.route("/subjects/delete/<subject>")
@login_required
def delete_subject(subject):
    if subject not in subjects.keys():
        abort(400)
    else:
        del subjects[subject]
        subjects.commit()
        return redirect("/admin")


@app.route("/subjects/add", methods=["POST", "GET"])
@login_required
def add_subject():
    if request.method == "GET":
        return render_template("add_subject.html")
    form = request.form
    subjects[form["subject"]] = [form["days"], 30, [int(str(i).strip()) for i in form["classes"].split(",")]]
    subjects.commit()
    return redirect("/admin")


if __name__ == '__main__':
    db_session.global_init("db/iti.db")
    # app.run(host="localhost")
    serve(app, host="localhost")
