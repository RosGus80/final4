from abc import ABC, abstractmethod
import json
import requests
from pprint import pprint as write

class ApiBase(ABC):

    @abstractmethod
    def get_page(self):
        """Метод для получения ответа от апи с соответствующими параметрами"""
        pass

    @abstractmethod
    def tofile(self, dict_to_reformat):
        """Метод для форматирования ответа в конкретного апи одинаковым способом"""
        pass

    @staticmethod
    def write(path, json_to_write):
        with open(path, "w") as file:
            for vacancy in json_to_write:
                file.write(json.dumps(vacancy, indent=2, ensure_ascii=False))
                file.write("\n")

    @abstractmethod
    def rmfile(self):
        """Метод для удаления вакансий из файла по фильтру"""
        pass

