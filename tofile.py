from abc import ABC, abstractmethod
import json
from vacancies import Vacancy
from pprint import pprint


class ToFile(ABC):

    @abstractmethod
    def tofile(self, reformat):
        """Метод для форматирования ответа конкретного апи одинаковым способом"""
        pass

    @staticmethod
    def write(path, vacs_to_write):
        """Статический метод для записи выбранных вакансий в файл в формате json"""
        output = []
        for vac in vacs_to_write:
            output.append(vac.__dict__)
        with open(path, "w") as file:
            file.write(str(json.dumps(output, indent=2, ensure_ascii=False)))

    @staticmethod
    def leave_best_tofile(reformat):
        vacs = [Vacancy(name=vacancy["name"], apply_url=vacancy["url"],
                        employer_name=vacancy["employer"], experience=vacancy["experience"],
                        area=vacancy["area"], salary={"from": vacancy["salary"],
                                                      "to": vacancy["salary"]}) for vacancy in
                reformat]

        for vac in vacs:
            if vac.salary["from"] is not None and vac.salary["to"] is not None:
                vac.salary = round((vac.salary["from"] + vac.salary["to"])/2)
            elif vac.salary["from"] is not None:
                vac.salary = vac.salary["from"]
            elif vac.salary["to"] is not None:
                vac.salary = vac.salary["to"]
            else:
                vac.salary = 0

        return vacs

    @staticmethod
    def leave_best(path, number):
        """Метод для удаления всех вакансий кроме лучших n по зарплате"""
        with open(path) as file:
            data = json.load(file)
            output = []
            for vac in data:
                if len(output) < number:
                    output.append(vac)
                    output = sorted(output, key=lambda d: d['salary'], reverse=True)
                    continue
                else:
                    for vacancy in output:
                        if vac["salary"] > vacancy["salary"]:
                            del(output[number-1])
                            output.append(vacancy)
                            break
                    output = sorted(output, key=lambda d: d['salary'], reverse=True)

        return output
