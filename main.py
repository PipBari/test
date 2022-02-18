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


def input_member(p=None):
    headers = {"app-id": "620e1ba31d484bfb25e26c0d", "Host": "dummyapi.io"}
    url = f"https://dummyapi.io/data/v1/user/{p}"
    # dannie = {
    #     "text": "wwwwwww",
    #     "image": "https://cdnn21.img.ria.ru/images/151546/28/1515462835_0:0:1036:587_600x0_80_0_0_a75f922e8b052d966122e1c9dc40feb4.jpg",
    #     "likes": 2,
    #     "tags": ["sdads"],
    #     "owner": "620e1ba31d484bfb25e26c0d"
    # }
    p = requests.get(url=url, headers=headers)
    print(p)


input_member()

# def main():
#     x = int(input(
#         "Введите число в промежутке <1(Если хотите узнать данные сотрудника) >=1(Если хотите внести нового сотрудника)"))
#     if x < 1:
#         q = input("Введите интересующий Вас ID:")
#         download(q)
#     else:
#
#
# main()
