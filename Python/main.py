import requests
from datetime import datetime, timedelta
import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename = "mylog.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

logging.info('Starting')

#Запрос к именам
url_name = requests.get('https://api.exchangerate.host/symbols').json()
X_name = url_name.get('symbols')

#Запрос к изменениям и дата
Date = datetime.now().date()
Thirty_days = Date - timedelta(days=30)
url = requests.get(f'https://api.exchangerate.host/fluctuation?start_date={Date}&end_date={Thirty_days}&base=EUR').json()
X = url.get("rates")

# Словарь со название валют
list_name = {}
for key, val in X_name.items():
    X_dis = X_name.get(key)
    list_name[key] = X_dis.get('description')


# Словарь с инф о валютах
list_cr = {}
for key, val in X.items():
    X_cr = X.get(key)
    list_cr[key] = X.get(key)

# Запись Названия валют в текстовый файл Валюта - курс
try:
    with open('rate.txt', 'w') as out:
        for key, val in list_cr.items():
            X_key = X.get(key)
            out.write('{} - {}\n'.format(key, X_key.get('start_rate')))
except:print("Что-то пошло не так при записи в файл")

# Запись Названия важных событий в лог
try:
    with open('alert.txt', 'w') as out:
        for key, val in list_cr.items():
            X_key = X.get(key)
            out.write('Name: {}    Change: {}    Start_rate: {}    End_rate: {}\n'.format(key, X_key.get('change'), X_key.get('start_rate'), X_key.get('end_rate')))
except:print("Что-то пошло не так при записи в файл")


