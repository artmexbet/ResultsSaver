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
    def __init__(self, name):
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
        with open(self.directory, "w", encoding="utf8") as f:
            json.dump(self, f, ensure_ascii=False)


class Day(JsonDB):
    def __init__(self, name, subjects_database: dict, day: int):
        super(Day, self).__init__(name)
        self.subject_database = subjects_database
        self.day = day

    def add_result(self, student_id, subject, score):
        if subject in self.subject_database.keys():
            try:
                self[student_id]['days'][self.day - 1][subject] = [score, -1]
            except IndexError:
                self[student_id]['days'].append({subject: [score, -1]})
            return 0
        else:
            return 1


if __name__ == '__main__':
    subjects = JsonDB("subjects.json")
    d = Day("test.json", subjects, 0)
    print(d.add_result("1", "physics", 10))
    d.commit()
