import requests
import json
from apis import ApiBase
from tofile import ToFile
from vacancies import Vacancy
from pprint import pprint


class SuperJob(ApiBase, ToFile):
    apikey = "v3.r.137573938.afe9266125a1a683478c5aafefd73d1b07688451.ea51c987304742717f2042af4b80a26cbff1be2b"

    def get_page(self, text=None, area=None, salaryFrom=None, salayTo=None):
        """Метод, получающий страницу вакансий с superjob с соотвтсвующими фильтрами:
                text: Фильтр по ключевым словам
                area: Фильтр по населенным пунктам (Принимает название населенного пункта)
                salary: фильтр по зарплате со значениями "от" и "до" желаемых значений
                Возвращает объект, который нужно переформатировать в JSON"""
        params = {
            "keyword": text,
            "payment_from": salaryFrom,
            "payment_to": salayTo,
            "town": area
        }
        return requests.get("https://api.superjob.ru/2.0/vacancies/", params, headers={'X-Api-App-Id': self.apikey})

    def tofile(self, reformat):
        """Первый шаг форматирования ответа. Принимает json или пайтон список из ответа superjob
        , инициализирует объекты и возвращает отформатированный список с объектами типа Vacancy"""
        vacs = [Vacancy(name=vacancy["profession"], apply_url=vacancy["link"],
                        employer_name=vacancy["firm_name"], experience=vacancy["experience"]["title"],
                        area=vacancy["town"]["title"], salary={"from": vacancy["payment_from"],
                                                               "to": vacancy["payment_to"]}) for vacancy in
                reformat["objects"]]

        for vac in vacs:
            if vac.salary["from"] != 0 and vac.salary["to"] != 0:
                vac.salary = round((vac.salary["from"] + vac.salary["to"])/2)
            elif vac.salary["from"] != 0:
                vac.salary = vac.salary["from"]
            elif vac.salary["to"] != 0:
                vac.salary = vac.salary["to"]
            else:
                vac.salary = 0

        return vacs


# a = SuperJob
# b = a.get_page(self=a, text="Python", area="Москва")
# c = b.json()
# d = a.tofile(a, c)
# a.write("vac.txt", d)