

class Vacancy:
    def __init__(self, name, apply_url, employer_name, experience, area, salary:dict):

        #self.number = number
        self.name = name
        self.url = apply_url
        self.employer = employer_name
        self.experience = experience
        self.area = area
        self.salary = {"from": salary["from"],
                       "to": salary["to"]}

        # if not self.salary["from"].isdigit() or self.salary["to"].isdigit():
        #     raise ValueError("Зарплата была указана не в численных значениях!")

    # def __eq__(self, other):
    #     return self.salary == other.salary
    #
    # def __gt__(self, other):
    #     return self.salary > other.salary
    #
    # def __lt__(self, other):
    #     return self.salary < other.salary
    #
    # def __ge__(self, other):
    #     return self.salary >= other.salary
    #
    # def __le__(self, other):
    #     return self.salary <= other.salary
    #
