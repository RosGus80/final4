from hh import HhApi
from superjob import SuperJob
import time


def print_vacancy(vacancy):
    print(f"Должность: {vacancy.name}")
    print(f"Работодатель: {vacancy.employer}")
    print(f"Опыт: {vacancy.experience}")
    print(f"Зарплата: {vacancy.salary}")
    print(f"Ссылка для отклика: {vacancy.url}")


def userinteraction():
    possible_town_input = ["1", "2", "3", "4", "5", "Москва", "Санкт-Петербург", "Казань", "Екатеринбург", "Самара"]

    print("Привет! Давай подберем тебе вакансию с сайтов поиска вакансий! Нажми Enter чтобы продолжить...")
    input()
    print("""Выбери населенный пункт из списка:
    1) Москва
    2) Санкт-Петербург
    3) Казань
    4) Екатеринбург
    5) Самара
    (Введи порядковый номер или название)
    """)

    while True:
        try:
            town_input = input().strip().title()
            if town_input not in possible_town_input:
                raise KeyError
            else:
                break
        except KeyError:
            print("Пожалуйста, введи номер или название города из списка")

    if town_input in ["1", "Москва"]:
        hh_area = "1"
        sj_area = "Москва"
    elif town_input in ["2", "Санкт-Петербург"]:
        hh_area = "2"
        sj_area = "Санкт-Петербург"
    elif town_input in ["3", "Казань"]:
        hh_area = "88"
        sj_area = "Казань"
    elif town_input in ["4", "Екатеринбург"]:
        hh_area = "3"
        sj_area = "Екатеринбург"
    elif town_input in ["5", "Самара"]:
        hh_area = "78"
        sj_area = "Самара"

    print("Отлично! Теперь введи пару ключевых слов о професси, которую ищешь "
          "(Например: Аналитик данных, ведущий экономист или просто Python)")
    user_keywords = input()
    print("Теперь введи примерную зарплату (в рублях), на которую расчитываешь (введи число)")
    while True:
        try:
            user_salary = int(input())
            break
        except ValueError:
            print("Пожалуйста, введи целое число")
    HH = HhApi
    SJ = SuperJob
    hh_page = HH.get_page(HH, user_keywords, hh_area, user_salary)
    sj_page = SJ.get_page(SJ, user_keywords, sj_area,
                          user_salary-(user_salary/100*30), user_salary+(user_salary/100*50))
    hh_json = hh_page.json()
    sj_json = sj_page.json()
    hh_filtered = HH.tofile(HH, hh_json)
    sj_filtered = SJ.tofile(SJ, sj_json)
    filtered = []
    filtered.extend(hh_filtered)
    filtered.extend(sj_filtered)
    HH.write("vac.txt", filtered)
    print(f"Отлично! Я нашел для тебя {len(filtered)} вакансий. "
          f"Скажи, сколько мне вывести лучших из них? (введи число от 1 до {len(filtered)})")
    while True:
        try:
            user_number = int(input())
        except ValueError:
            print("Пожалуйста, введи число")
            continue
        if 0 < user_number <= len(filtered):
            break
        else:
            print(f"Пожалуйста, введи число от 1 до {len(filtered)}")

    best = HH.leave_best("vac.txt", user_number)
    tofiled_best = HH.leave_best_tofile(best)
    HH.write("vac.txt", tofiled_best)

    print("Вот лучшие из вакансий, что я нашел:")
    time.sleep(1.5)
    for vac in tofiled_best:
        print_vacancy(vac)
        print()

    print("Всего доброго!")


if __name__ == "__main__":
    userinteraction()
