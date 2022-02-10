import requests
import json


def download(q: str):
    url = f"http://dummy.restapiexample.com/api/v1/employees{q}&1"
    r = requests.get(url)
    if r.status_code == 200:
        print(r.json())
    else:
        print(r.status_code)


def input_member(p: str):
    url = f"http://dummy.restapiexample.com/api/v1/create{p}"
    p = requests.post(url, json)


def main() -> None:
    x = int(input("Введите число в промежутке <1(Если хотите узнать данные сотрудника) >=1(Если хотите внести нового сотрудника)"))
    if x < 1:
        q = input("Введите интересующий Вас ID:")
        download(q)
    else:
        p = input("Введите Ф.И.О нового сотрудника:")
        input_member(p)
