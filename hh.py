from abc import ABC, abstractmethod
import json
import requests
from pprint import pprint as write
from apis import ApiBase

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
        for vacancie in reformat["items"]:
            output.append({
                "name": vacancie["name"],
                "apply_url": vacancie["apply_alternate_url"],
                "employer": {
                    "name": vacancie["employer"]["name"],
                    "url": vacancie["employer"]["alternate_url"]
                },
                "experience": vacancie["experience"]["name"],
                "salary": f"От {vacancie['salary']['from']} до {vacancie['salary']['to']}",
            })
        return output





a = HhApi
b = a.get_page(self=a, text="Python", area=1, salary=100_000, only_with_salary=True)
c = b.json()
# write(c)
# for i in range(5):
#     print(c["items"][i]["name"])
#     print(c["items"][i]["snippet"]["requirement"])
#     print(c["items"][i]["snippet"]["responsibility"])
#     print()

d = a.tofile(a, c)
a.write("vac.txt", d)



