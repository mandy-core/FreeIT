from math import sqrt
import time
from tkinter.messagebox import NO
from types import ModuleType
from openpyxl import Workbook

# Task 1
def write_text_to_file(path, method, content):
    with open(path, method) as text:
        text.write(content)
        print(content)
write_text_to_file('E:\Course\Task/text.txt','w', 'Доброго вечора ми з України')



#Task 2
def season(month):
    if 12 == month <= 2:
        print('Зима')
    elif month <= 5:
        print('Весна')
    elif month <= 8:
        print('Лето')
    else:
        print('Осень')
season(9)



# Task 3
def square(a):
	p = a*4
	s = a*a
	d = sqrt(a**2 + a**2)
	karteg = (p, s, d)
	return karteg
print(square(5))



# Task 4
def bank(years, amount):
 
    a = 0
    c_amount = 0
    while a < years:
        a += 1
        c_amount = amount*(1+0.1)**years   
    print('Вы получили = ' + str(c_amount))

years = int(input('На сколько лет? '))
amount = int(input('Сумма? '))
bank(years, amount)



# Task 5

def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"Функция выполнена за {end_time:4f}сек")
        return value
    return wrapper_decorator


@decorator
def some_func(num):
    while num < 4:
        num += 1
        print("1 sec left")
        time.sleep(1)
some_func(2)
