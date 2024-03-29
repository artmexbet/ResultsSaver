import json
import os
from copy import deepcopy

import openpyxl
from openpyxl import Workbook


class SubjectIsAlreadyExists(Exception):
    pass


def save_xlsx_file(filename, byte_data) -> Workbook:
    """
    Функция создаёт xlsx файл из полученного массива байт.
    :param filename: Имя файла, в котоырй будет сохранён массив байт
    :type filename: str
    :param byte_data: Массив байт
    :type byte_data: bytes
    :return: Файл xlsx
    """
    directory = f"temp_files/{filename}"
    with open(directory, "wb") as file:
        file.write(byte_data)
    return openpyxl.load_workbook(directory)


class JsonDB(dict):
    def __init__(self, name: str, value: dict = None):
        """
        Базовый класс-API для работы с БД на JSON
        :param name: имя файла С ТИПОМ ("test.json")
        """
        self.directory = f"databases/{name}"
        if not os.path.exists(self.directory):
            if value:
                super().__init__(value)
            else:
                super().__init__({})
            self.commit()
        else:
            with open(self.directory, encoding="utf8") as f:
                js = json.load(f)
            super().__init__(js)

    def __getitem__(self, item):
        if item in self.keys():
            return self.get(item)
        else:
            raise KeyError("Такого ключа не существует")

    def __str__(self):
        return self

    def get_from_key(self, key, value):
        for i, elem in enumerate(self["data"]):
            if key in elem and elem[key] == value:
                return self["data"][i]

    def commit(self):
        """
        Функция сохранения
        :return:
        """
        with open(self.directory, "w", encoding="utf8") as f:
            json.dump(self, f, ensure_ascii=False)


class Day(JsonDB):
    def __init__(self, name, subjects_database: dict, data: dict = None):
        """
        Класс для работы с участниками. Для каждого года
        создаётся новая база данных (возможно скопируем эту, только без данных).
        Класс наследован от базового класса БД.
        :param name: имя файла С ТИПОМ ("test.json")
        :param subjects_database: база данных предметов, также создаётся каждый год
        """
        directory = f"databases/{name}"
        if not os.path.exists(directory):
            if data:
                super(Day, self).__init__(name, data)
            else:
                super(Day, self).__init__(name, {"users": []})
        else:
            super(Day, self).__init__(name)
        self.subject_database = subjects_database
        self.day = 0

    def add_result(self, subject: str, score: int, student: dict):
        """
        Этот метод присваивает пользователю результат
        :param subject: предмет
        :param score: результат
        :param student: информация об ученике
        :return:
        """
        if subject in self.subject_database.keys():
            if self.day == self.subject_database[subject][0] - 1:
                student['days'][self.day][subject] = [score, -1]
                self.commit()
                return {"verdict": "ok"}, 200  # Всё прошло успешно
            else:
                return {"verdict": "This subject doesn't exist today"}, 401  # Этого предмета в этот день нет
        else:
            return {"verdict": "This subject doesn't exist"}, 404  # Такого предмета не существует

    def set_day(self, new_day=None):
        if new_day is not None:
            self.day = new_day
        else:
            self.day += 1

    def remove(self, item):
        for i in range(len(self["users"])):
            if self["users"][i]["id"] == item["id"]:
                del self["users"][i]
                self.commit()
                break

    def get_item_with_id(self, item_id: int) -> dict:
        for i in range(len(self["users"])):
            if item_id == self["users"][i]["id"]:
                return self["users"][i]
        raise KeyError("Такого ключа не существует!")

    def get_items_with_class(self, class_dig: int) -> list:
        if class_dig not in range(5, 10):
            raise IndexError(f"Class digit must be in range(5, 10), not {class_dig}")
        return list(filter(lambda x: x["class"] == class_dig, self["users"]))

    def find_item_with_subjects(self, subject: str) -> list:
        temp = list(filter(lambda x: subject in [k for j in x["days"] for k in j.keys()], self["users"]))
        for i, student in enumerate(temp):
            temp_subjects = {k[0]: k[1] for i in student["days"] for k in i.items()}
            temp[i][subject] = temp_subjects[subject]
        return temp

    @property
    def get_last_id(self):
        return self["users"][-1]["id"] + 1

    def add_user(self, user):
        user["id"] = self.get_last_id
        self["users"].append(user)
        self.commit()

    @property
    def get_ids(self):
        return [i["id"] for i in self["users"]]

    @property
    def results(self) -> dict:
        """Эта штуковина возвращает результаты участников по id и классам"""
        temp_results = {}
        for user_id in self.get_ids:
            temp = self.get_item_with_id(user_id)
            temp_results[user_id] = {"class": temp["class"]}
            temp_days = temp["days"][self.day].copy()
            for subject in temp_days.keys():
                temp_results[user_id][subject] = temp_days[subject][0]
        return temp_results
        # for index in range(len(self["users"])):
        #     temp_results[index] = {"class": self["users"][index]["class"]}
        #     for result in self["users"][index]["days"][self.day].keys():
        #         temp_results[index][result] = self["users"][index]["days"][self.day][result][0]
        # return temp_results

    @property
    def classes_count(self) -> tuple:
        temp = {self["users"][index]["class"] for index in range(len(self["users"]))}
        return min(temp), max(temp) + 1

    @property
    def count_teams(self):
        teams = {}
        betters_users = convert_to_betters(self["users"])
        for user in betters_users:
            if user["team"]:
                try:
                    teams[user["team"]] += sum(user["results"].values())
                except Exception as ex:
                    print(ex)
                    teams[user["team"]] = sum(user["results"].values())
        return [{"team_name": key, "team_results": value} for key, value in sorted(teams.items(), key=lambda x: -x[1])]


class Config:
    def __init__(self):
        with open("site_config.json", encoding="utf8") as config:
            self.config = json.load(config)

    @property
    def day(self) -> int:
        try:
            return self.config["day"]
        except Exception as ex:
            print(ex)

    @property
    def current_subjects(self) -> str:
        try:
            return self.config["current_subjects"]
        except Exception as ex:
            print(ex)

    @property
    def current_students(self) -> str:
        try:
            return self.config["current_students"]
        except Exception as ex:
            print(ex)

    @property
    def current_admins(self) -> str:
        try:
            return self.config["current_admins"]
        except Exception as ex:
            print(ex)

    @property
    def opened_day(self):
        try:
            return self.config["opened_day"]
        except Exception as ex:
            print(ex)

    @property
    def configs(self) -> tuple:
        try:
            return self.day, self.current_subjects, self.current_students, self.current_admins, self.opened_day
        except Exception as ex:
            print(ex)

    def set_configs(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.config.keys():
                self.config[key] = value
            else:
                raise KeyError("Такого ключа не существует!")
        self.commit()

    def commit(self):
        with open("site_config.json", "w") as file:
            json.dump(self.config, file, ensure_ascii=False)


def is_data_edited(name: str, days: Day) -> bool:
    """Проверяет, есть ли такой человек в бд."""
    # ids = [i["id"] for i in days["users"]]
    for i in days["users"]:
        if name == i["name"]:
            return True
    return False


def json_from_xlsx(file: Workbook, days: Day):
    wb = file.active
    # student_i = list(range(1000, 50000))
    # shuffle(student_i)
    days["users"] = []
    for i in list(wb.rows)[1::]:
        student_id, name, stage, *rubbish = [k.value for k in i]
        if not name or is_data_edited(name, days):
            continue
        try:
            class_digit = stage[:-1]
            class_letter = stage[-1]
        except TypeError:
            class_digit = stage
            class_letter = ""
        days["users"].append({
            "id": student_id,
            "name": name,
            "class": int(class_digit),
            "class_letter": class_letter,
            "days": [{}, {}],
            "team": ""})
    days.commit()


def all_subject_results(results: dict, subject, class_digit) -> (dict, int):
    """Возвращает результаты всех участников по предмету (subject) из определённого класса (class_digit)"""
    temp = {}
    for key in results.keys():
        if subject in results[key].keys() and results[key]["class"] == class_digit:
            temp[key] = results[key][subject]
    if temp:
        return temp


def student_sum(student: dict) -> int:
    return sum([int(k[1]) for j in student['days'] for k in j.values()])


def recount(day: Day, all_subjects: JsonDB) -> dict:
    classes = day.classes_count
    a = day.results
    for subject in all_subjects.keys():
        for class_digit in range(*classes):
            subject_result = all_subject_results(a, subject, class_digit)
            if subject_result:
                user_id, max_result = max(subject_result.items(), key=lambda x: x[1])
                if max_result > all_subjects[subject][1] / 2:
                    percent = max_result / 100
                else:
                    percent = all_subjects[subject][1] / 200
                for i, val in subject_result.items():
                    day.get_item_with_id(i)["days"][day.day][subject][1] = round(val / percent, 1)
    day.commit()
    return {"verdict": "ok"}


def get_subject_result(student: dict, subject: str) -> float:
    for i in student["days"]:
        if subject in i.keys():
            return i[subject]
    raise KeyError("Такого ключа не существует!")


def convert_to_betters(users: list) -> list:
    day = deepcopy(users)
    for user_ind in range(len(day)):
        results = sorted(
            {subject: result[1] for users_day in day[user_ind]["days"] for subject, result in
             users_day.items()}.items(),
            key=lambda x: -x[1])
        day[user_ind].pop("days")
        day[user_ind]["results"] = {key: value for key, value in results}
    return day


if __name__ == '__main__':
    subjects = JsonDB("subjects.json")
    d = Day("test1.json", subjects)
    d.set_day(1)
    print(d.day)
