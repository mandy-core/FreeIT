import requests
from datetime import datetime, timedelta

#Запрос к именам
url_name = 'https://api.exchangerate.host/symbols'
response_name = requests.get(url_name)
data_name = response_name.json()
X_name = data_name.get('symbols')
#Запрос к изменениям и дата
Date = datetime.now().date()
Thirty_days = Date - timedelta(days=30)
url = f'https://api.exchangerate.host/fluctuation?start_date={Date}&end_date={Thirty_days}&base=EUR'
response = requests.get(url)
data = response.json()
X = data.get("rates")

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
with open('rate.txt', 'w') as out:
    for key, val in list_cr.items():
        X_key = X.get(key)
        out.write('{} - {}\n'.format(key, X_key.get('start_rate')))

# Запись Названия важных событий в лог
with open('alert.log', 'w') as out:
    for key, val in list_cr.items():
        X_key = X.get(key)
        out.write('Name: {}    Change: {}    Start_rate: {}    End_rate: {}\n'.format(key, X_key.get('change'), X_key.get('start_rate'), X_key.get('end_rate')))
