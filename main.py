from hh import HhApi
from superjob import SuperJob
import time

def print_vacancy(vacancy):
    print(f"Должность: {vacancy.name}")
    print(f"Работодатель: {vacancy.employer}")
    print(f"Опыт: {vacancy.experience}")
    print(f"Зарплата: {vacancy.salary}")
    print(f"Ссылка для отклика: {vacancy.url}")

def UserInteraction():
    print("Привет! Давай подберем тебе вакансию с сайтов поиска вакансий! Нажми Enter чтобы продолжить...")
    input()
    #print("Введи населенный пункт, в котором ты живешь: ", end="")
    #user_area = input()
    user_area = 1
    print("Отлично! Теперь введи пару ключевых слов о професси, которую ищешь "
          "(Например: Аналитик данных, ведущий экономист или просто Python)")
    user_keywords = input()
    print("Теперь введи примерную зарплату, на которую расчитываешь (введи число)")
    user_salary = int(input())
    HH = HhApi
    SJ = SuperJob
    hh_page = HH.get_page(HH, user_keywords, user_area, user_salary)
    sj_page = SJ.get_page(SJ, user_keywords, "Москва", user_salary-(user_salary/100*30), user_salary+(user_salary/100*50))
    hh_json = hh_page.json()
    sj_json = sj_page.json()
    hh_filtered = HH.tofile(HH, hh_json)
    sj_filtered = SJ.tofile(SJ, sj_json)
    filtered = []
    filtered.extend(hh_filtered)
    filtered.extend(sj_filtered)
    HH.write("vac.txt", filtered)
    print("Отлично! Я нашел для тебя вакансии. Скажи, сколько мне вывести лучших из них? (введи число от 0 до 40)")
    user_number = int(input())
    best = HH.leave_best("vac.txt", user_number)
    tofiled_best = HH.leave_best_tofile(best)
    HH.write("vac.txt", tofiled_best)

    print("Вот лучшие из вакансий, что я нашел:")
    time.sleep(1.5)
    for vac in tofiled_best:
        print_vacancy(vac)
        print()

    print("Всего доброго!")


UserInteraction()