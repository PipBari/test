import requests
import json


def download(q=None):
    headers = {"Connection": "keep-alive",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
               "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US;q=0.8"}
    url = f"http://dummy.restapiexample.com/api/v1/employee/{q}"
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        print(r.json())
    else:
        print(r.status_code)


def new_id():
    headers = {"app-id": "620e1ba31d484bfb25e26c0d", "host": "dummyapi.io"}
    url = f"https://dummyapi.io/data/v1/user/create"
    information = {"firstName": "Aboba", "lastName": "Abobas", "email": "QWEZXC@aaaa.com"}
    re = requests.post(url=url, json=information, headers=headers)


def new_post():
    headers = {"app-id": "620e1ba31d484bfb25e26c0d", "host": "dummyapi.io"}
    url = f"https://dummyapi.io/data/v1/user/create"
    data_inf = {"text", "image", "likes", "tags", "owner"}
    res = requests.post(url=url, json=data_inf, headers=headers)
    if res.status_code == 200:
        print(res.status_code)
    else:
        print(res.status_code)


def main():
    x = int(input(
        "Введите число в промежутке <1(Если хотите узнать данные сотрудника) >=1(Если хотите внести нового сотрудника)"))
    if x < 1:
        q = input("Введите интересующий Вас ID:")
        download(q)
    else:
        k = {
            "text": string(input("Введите текст:"))
            "image": string(input("Введите ссылку:"))

        }
    new_post(k)


main()
