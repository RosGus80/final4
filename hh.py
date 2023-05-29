import requests
from apis import ApiBase
from tofile import ToFile
from vacancies import Vacancy
import pprint


class HhApi(ApiBase, ToFile):

    def get_page(self, text=None, area=None, salary=None):
        """Метод, получающий страницу вакансий с hh.ru с соотвтсвующими фильтрами:
        text: Фильтр по ключевым словам
        area: Фильтр по населенным пунктам (принимает айди пункта в формате int)
        salary: фильтр по зарплате (в итоговом формате учитывается только вилка зарплаты)
        Возвращает объект, который нужно переформатировать в JSON"""
        if text is not None:
            text = "+".join(text.split(" "))
            params = {"text": f"NAME:{text}", "area": area, "salary": salary, "only_with_salary": True}
        else:
            params = {"area": area, "salary": salary, "only_with_salary": True}

        return requests.get("https://api.hh.ru/vacancies", params)

    def tofile(self, reformat):
        """Первый шаг форматирования ответа. Принимает json или пайтон список из ответа hh.ru
        , инициализирует объекты и возвращает отформатированный список с объектами типа Vacancy"""
        vacs = [Vacancy(name=vacancy["name"], apply_url=vacancy["apply_alternate_url"],
                        employer_name=vacancy["employer"]["name"], experience=vacancy["experience"]["name"],
                        area=vacancy["area"]["name"], salary={"from": vacancy["salary"]["from"],
                                                              "to": vacancy["salary"]["to"]}) for vacancy in
                reformat["items"]]

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


# a = HhApi
# # b = a.get_page(self=a, text="Экономист", area=1, salary=150_000)
# # c = b.json()
# # d = a.tofile(self=a, reformat=c)
# #
# # a.write("vac.txt", d)
# e = a.leave_best("vac.txt", 10)
# f = a.leave_best_tofile(e)
# a.write("vac.txt", f)
