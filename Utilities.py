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
    :type byte_data: bytearray
    :return: Файл xlsx
    """
    directory = f"temp_files/{filename}"
    with open(directory, "wb") as file:
        file.write(byte_data)
    return openpyxl.load_workbook(directory)


class JsonDB(dict):
    def __init__(self, name, data=None):
        self.directory = f"databases/{name}"
        if not data:
            data = {}
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
            json.dump(self, f, ensure_ascii=True)


class Day(JsonDB):
    def __init__(self, name, data=None):
        super(Day, self).__init__(name, data)

    def __setitem__(self, key, value):
        if key not in self.keys():
            raise KeyError("Такого ключа не существует! Для добавления ключа используйте метод"
                           "add_subject")
        else:
            self[key] = value

    def add_subject(self, subject_name):
        if subject_name in self[list(self.keys())[0]][0].keys():
            raise KeyError("Такой ключ уже существует!")
        for i in self.keys():
            self[i][0][subject_name] = -1
            self[i][1][subject_name] = -1


if __name__ == '__main__':
    d = Day("test.json")
    d.add_subject("a")
    # d.add_subject("a")
    d.commit()
