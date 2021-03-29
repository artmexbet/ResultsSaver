import openpyxl
import json
import os

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

    def __setitem__(self, key, value):
        self[key] = value

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

    def add_result(self, student_id: int, subject: str, score: int):
        """
        Этот метод присваивает пользователю результат
        :param student_id: id студента
        :param subject: предмет
        :param score: результат
        :return:
        """
        if subject in self.subject_database.keys():
            if self.day == self.subject_database[subject][0] - 1:
                try:
                    self["users"][student_id - 1]['days'][self.day][subject] = [score, -1]
                except IndexError:
                    self["users"][student_id - 1]['days'].append({subject: [score, -1]})
                return {"verdict": "ok"}  # Всё прошло успешно
            else:
                return {"verdict": "This subject doesn't exist today"}  # Этого предмета в этот день нет
        else:
            return {"verdict": "This subject doesn't exist"}  # Такого предмета не существует

    def set_day(self, new_day=None):
        if new_day:
            self.day = new_day
        else:
            self.day += 1

    def remove(self, item):
        for i in range(len(self["users"])):
            if self["users"][i] == item:
                del self["users"][i]

    def get_item_with_id(self, id: int) -> dict:
        for i in range(len(self["users"])):
            if id == self["users"][i]["id"]:
                return self["users"][i]

    def find_item_with_class(self, class_dig: int) -> list:
        if class_dig not in range(5, 10):
            raise IndexError(f"Class digit must be in range(5, 10), not {class_dig}")
        return list(filter(lambda x: x["class"] == class_dig, self["users"]))

    def find_item_with_subjects(self, subject: str) -> list:
        temp = list(filter(lambda x: subject in [k for i in x["days"] for k in i.keys()], self["users"]))
        for i, student in enumerate(temp):
            subjects = {k[0]: k[1] for i in student["days"] for k in i.items()}
            temp[i][subject] = subjects[subject]
        return temp

    @property
    def get_last_id(self):
        return self["users"][-1]["id"] + 1

    def add_user(self, user):
        user["id"] = self.get_last_id()
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
            temp_days = temp["days"][self.day]
            for result in temp_days.keys():
                temp_results[user_id][result] = temp_days[result][0]
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


def is_data_edited(student_id: int, name, stage, days: Day) -> bool:
    ids = [i["id"] for i in days["users"]]
    for i in days["users"]:
        if (student_id == i["id"] and (name != i["name"] or stage != i["class"])) or student_id not in ids:
            return True
    return False


def json_from_xlsx(file: Workbook, days: Day):
    wb = file.active
    for i in list(wb.rows)[1::]:
        student_id, name, stage, *rubbish = [k.value for k in i]
        if not is_data_edited(student_id, name, stage, days):
            continue
        if not name:
            continue
        try:
            class_digit = stage[:-1]
            class_letter = stage[-1]
        except TypeError:
            class_digit = stage
            class_letter = ""
        days["users"].append({
            "id": i,
            "name": name,
            "class": int(class_digit),
            "class_letter": class_letter,
            "days": []})
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
    for subject in all_subjects.keys():
        for class_digit in range(*day.classes_count):
            subject_result = all_subject_results(day.results, subject, class_digit)
            print(subject_result)
            if subject_result:
                user_id, max_result = max(subject_result.items(), key=lambda x: x[1])
                if max_result > all_subjects[subject][1] / 2:
                    percent = max_result / 100
                else:
                    percent = all_subjects[subject][1] / 200
                for i, val in subject_result.items():
                    day.get_item_with_id(user_id)["days"][day.day][subject][1] = round(val / percent, 1)
                day.commit()
    return {"verdict": "ok"}


def sorting(day: Day):
    day["users"].sort(key=lambda x: x["id"])
    day.commit()


if __name__ == '__main__':
    subjects_test = JsonDB("subjects.json")
    d_test = Day("test.json", subjects_test)
    recount(d_test, subjects_test)
    print(d_test.results)
