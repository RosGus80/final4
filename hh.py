from abc import ABC, abstractmethod
import json
import requests
from apis import ApiBase
import pprint

class HhApi(ApiBase):

    def get_page(self, text=None, area=None, salary=None, only_with_salary=False):
        if text is not None:
            text = "+".join(text.split(" "))
            params = {"text": f"NAME:{text}", "area": area, "salary": salary, "only_with_salary": only_with_salary}
        else:
            params = {"area": area, "salary": salary}

        return requests.get("https://api.hh.ru/vacancies", params)

    def tofile(self, reformat):
        output = []
        for vacancy in reformat["items"]:
            output.append({
                "name": vacancy["name"],
                "apply_url": vacancy["apply_alternate_url"],
                "employer": {
                    "name": vacancy["employer"]["name"],
                    "url": vacancy["employer"]["alternate_url"]
                },
                "experience": vacancy["experience"]["name"],
                "area": vacancy["area"]["name"],
                "salary": {"from": vacancy["salary"]["from"],
                           "to": vacancy["salary"]["to"]}
            })
        return output





a = HhApi
b = a.get_page(self=a, text="Python", area=1, salary=100_000, only_with_salary=True)
c = b.json()
d = a.tofile(self=a, reformat=c)

a.write("vac.txt", d)
with open("vac.txt") as file:
    e = json.load(file)

pprint.pprint(e)
