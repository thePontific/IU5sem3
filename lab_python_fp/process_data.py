import json
import sys
from random import randint
from cm_timer import cm_timer_1
from print_result import print_result
from unique import Unique

path = "data_light.json"
with open(path, encoding="utf-8") as f:
    data = json.load(f)

@print_result
def f1(arg):
    # уник проф игнорируем регист
    return sorted(Unique([job["job-name"] for job in arg], ignore_case=True), key=str.lower)

@print_result
def f2(arg):
    # программист, начинается с!!
    return list(filter(lambda x: x.lower().startswith("программист"), arg))

@print_result
def f3(arg):
    #опыт питон добавить строчку
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    # зарплата
    salaries = [randint(100_000, 200_000) for _ in arg]
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]
# зип объединяет список профессий и список зарплаты создавая новый типо "{job},{salary} руб."
if __name__ == "__main__":
    with cm_timer_1():
        f4(f3(f2(f1(data))))
