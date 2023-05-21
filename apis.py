from abc import ABC, abstractmethod
import json
import requests
import pprint


class ApiBase(ABC):

    @abstractmethod
    def get_page(self):
        """Метод для получения ответа от апи с соответствующими параметрами"""
        pass

    @staticmethod
    def tofile(reformat):
        """Метод для форматирования ответа в конкретного апи одинаковым способом"""
        pass

    @staticmethod
    def write(path, json_to_write):
        """Статический метод для записи выбранных вакансий в файл в формате json"""
        with open(path, "w") as file:
            file.write(str(json.dumps(json_to_write, indent=2, ensure_ascii=False)))

    @staticmethod
    def rmfile(path, text=None, area=None, salary=None, only_with_salary=None):
        """Метод для удаления вакансий из файла по фильтру.
        Без передачи аргументов удаляет все записи в файле"""
        pass


