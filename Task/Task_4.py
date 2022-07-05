from copy import copy, deepcopy
import os
import datetime
import re
from time import time
import random
import time


#// Задание 4.1
lst_a = list(range (0, 11))
lst_b = deepcopy(lst_a)
c_dictionary = dict(zip(lst_b, lst_a))
print(c_dictionary)


#// Задине 4.2
d1 = {"a" : 1}
d2 = {"b" : 2}
d2["b"] = 5
# Решение при помощи оператра
d3_opr =  d1 | d2
print(d3_opr)
# Решение циклом
d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value
print(d3)
# Решение способом update
d1.update(d2)
d3_upd = deepcopy(d1)
print(d3_upd)


#// Задине 4.3
d1_change = {"key1": 1, "key2": 2}
inverse_d1 = {}
for key,value in d1_change.items():
    inverse_d1[value]=key
print(inverse_d1)
#Альтернативное решение
d1_alt=dict(zip(d1_change.values(),d1_change.keys()))
print(d1_alt)


#// Задине 4.4
dirname= 'E:\Course\Task'
files = os.listdir(dirname)
print(files)


#// Задине 4.5
time_now = datetime.datetime.now()
print (time_now.strftime("%d-%m-%Y %H:%M"))

#// Задине 4.6
a = 0
while a<10:
    input('Нажми Enter')
    print (a)
    a = a+1


#// Задаие 4.7
string = 'LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAK'
print(re.sub(r'[A-Z]', '', string))


#// Задаие 4.8
colors = ["красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"]
num_color = 1
for x in colors:

    print (num_color, 'Цвет радуги',str.title(x))
    num_color += 1


#// Задаие 4.9
x = time.time()
z = 0
while time.time() < x + 10:
    print(z)
    z += 1

#// Задания 4.10
x = 1

while x < 10:
    print(str(x) * x ) 
    x+=1