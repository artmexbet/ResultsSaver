import openpyxl
import json
import os


class SubjectIsAlreadyExists(Exception):
    pass


def save_xlsx_file(filename, byte_data):
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

    def commit(self):
        """
        Функция сохранения
        :return:
        """
        with open(self.directory, "w", encoding="utf8") as f:
            json.dump(self, f, ensure_ascii=False)


class Day(JsonDB):
    def __init__(self, name, subjects_database: dict):
        """
        Класс для работы с участниками. Для каждого года
        создаётся новая база данных (возможно скопируем эту, только без данных).
        Класс наследован от базового класса БД.
        :param name: имя файла С ТИПОМ ("test.json")
        :param subjects_database: база данных предметов, также создаётся каждый год
        """
        directory = f"databases/{name}"
        if not os.path.exists(directory):
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
                return 0  # Всё прошло успешно
            else:
                return 2  # Этого предмета в этот день нет
        else:
            return 1  # Такого предмета не существует

    def set_day(self, new_day=None):
        if new_day:
            self.day = new_day
        else:
            self.day += 1

    @property
    def results(self) -> dict:
        """Эта штуковина возвращает результаты участников по id и классам"""
        temp_results = {}
        for index in range(len(self["users"])):
            temp_results[index] = {"class": self["users"][index]["class"]}
            for result in self["users"][index]["days"][self.day].keys():
                temp_results[index][result] = self["users"][index]["days"][self.day][result][0]
        return temp_results

    @property
    def classes_count(self) -> tuple:
        temp = {self["users"][index]["class"] for index in range(len(self["users"]))}
        return min(temp), max(temp) + 1


def all_subject_results(results: dict, subject, class_digit) -> (dict, int):
    temp = {}
    for key in results.keys():
        if subject in results[key].keys() and results[key]["class"] == class_digit:
            temp[key] = results[key][subject]
    if not len(temp):
        return 5
    return temp


def recount(day: Day, all_subjects: JsonDB) -> int:
    for subject in all_subjects.keys():
        for class_digit in range(*day.classes_count):
            subject_result = all_subject_results(day.results, subject, class_digit)
            print(subject_result)
            if isinstance(subject_result, dict):
                user_id, max_result = max(subject_result.items(), key=lambda x: x[1])
                if max_result > all_subjects[subject][1] / 2:
                    percent = max_result / 100
                else:
                    percent = all_subjects[subject][1] / 200
                for i, val in subject_result.items():
                    day["users"][user_id]["days"][day.day][subject][1] = val / percent
                day.commit()
    return 1


def sorting(day: Day):
    day["users"].sort(lambda x: x["id"])
    day.commit()


if __name__ == '__main__':
    subjects_test = JsonDB("subjects.json")
    d_test = Day("test.json", subjects_test)
    recount(d_test, subjects_test)
    print(d_test.results)
