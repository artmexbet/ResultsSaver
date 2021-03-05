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
    def __init__(self, name: str):
        """
        Базовый класс-API для работы с БД на JSON
        :param name: имя файла С ТИПОМ ("test.json")
        """
        self.directory = f"databases/{name}"
        if not os.path.exists(self.directory):
            self.commit()
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
        super(Day, self).__init__(name)
        self.subject_database = subjects_database
        self.day = 0

    def add_result(self, student_id: str, subject: str, score: int):
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
                    self[student_id]['days'][self.day][subject] = [score, -1]
                except IndexError:
                    self[student_id]['days'].append({subject: [score, -1]})
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
        temp_results = {}
        for key in self.keys():
            temp_results[key] = {}
            for result in self[key]["days"][self.day].keys():
                temp_results[key][result] = self[key]["days"][self.day][result][0]
        return temp_results


def all_subject_results(results, subject) -> (dict, int):
    # pass
    temp = {}
    for key in results.keys():
        if subject in results[key].keys():
            temp[key] = results[key][subject]
    if not len(temp):
        return 5
    return temp


def recount(day: Day, all_subjects: JsonDB) -> int:
    # pass
    for subject in all_subjects.keys():
        subject_result = all_subject_results(day.results, subject)
        max_result = max(subject_result)
        pass


if __name__ == '__main__':
    subjects = JsonDB("subjects.json")
    d = Day("test.json", subjects)
    print(d.results)
