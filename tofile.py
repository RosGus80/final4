from abc import ABC, abstractmethod
import json

class ToFile(ABC):

    @abstractmethod
    def tofile(self, reformat):
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
