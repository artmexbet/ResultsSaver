from flask import Flask, request, jsonify, render_template, redirect
from Utilities import *
from datetime import datetime
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, login_required, login_user, logout_user
import logging
from data import db_session
from data.admins import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["SECRET_KEY"] = "abrakadabra-key"
cors = CORS(app)
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
@cross_origin()
def main():
    return render_template("main.html", day=1, users=users_per_day(0))


@app.route('/register', methods=['GET', 'POST'])
@login_required
def reqister():
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
    logging.info("An DataBase was created by excel table")
    # sorting(d)
    return {"verdict": "ok"}, 200


@app.route("/users/<int:day>/<int:user_id>", methods=["post", "get"])
@cross_origin()
def get_user(day, user_id):
    try:
        if request.method == "GET":
            user = d.get_item_with_id(user_id).copy()
            temp_result = [{"subject": key, "value": value} for key, value in user["days"][day].items()]
            user["results"] = temp_result
            user.pop("days")
            logging.info("Info about users was received")
            return render_template("more.html", user=user)
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


def replace_results():
    global d
    data = request.get_json()
    d = Day(d.directory.split("/")[1], subjects, data)
    return {"verdict": "ok"}, 200


def patch_users(id, data: dict):
    item = d.get_item_with_id(id)
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
@cross_origin()
def all_sum():
    result = {'users': deepcopy(d['users'])}
    for i in result['users']:
        i['result'] = student_sum(i)
        del i['days']
    return result, 200


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
        logging.error(f"An error occurred: {ex} \n during adding some results")
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


def recount_main():
    # Пример запроса смотрите в файле recount_example.json
    recount(d, subjects)
    return {"verdict": "ok"}, 200


def add_user():
    data = request.get_json()
    d.add_user(data)
    return {"verdict": "ok"}, 200


# @app.route("/check_admins", methods=["POST"])
# @cross_origin()
# def check_admins():
#     data = request.get_json()
#     try:
#         if any(map(lambda x: x["login"] == data["login"] and x["password"] == data["password"], admins["data"])):
#             return {"data": {"access": 1, "speciality": admins.get_from_key("login", data["login"])["subject"]}}, 200
#         return {"data": {"access": 0}}, 200
#     except Exception as ex:
#         print(ex)
#         return {"error": "BadRequest"}, 400


def route_new_db():
    new_db(request.get_json())


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


def delete_user():
    data = request.get_json()
    try:
        d.remove(d.get_item_with_id(data["id"]))
        return {"verdict": "ok"}, 200
    except Exception as ex:
        print(ex)
        return {"error": "BadRequest"}, 400


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
@login_required
def get_admins():
    sess = db_session.create_session()
    return render_template("admins_list.html", admins=sess.query(Admin).all()), 200


@app.route("/users/betters/teams")
@cross_origin()
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


@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/iti.db")
    app.run(host="localhost")
