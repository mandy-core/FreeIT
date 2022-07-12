from math import sqrt
import time
from types import ModuleType



# Task 1
def do_operation(path, method, content):
    f = open(path, method)
    f.write(content)
    print(content)
    f.close
do_operation('E:\Course\Task/1111.txt','w', 'Доброго вечора ми з України')



#Task 2
def season(month):
    if month == 12 or month <= 2:
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
def outer():
    start_time = time.time()
    def inner():
        nonlocal start_time
        print("--- %s seconds ---" % (time.time() - start_time))
    return inner
outer()()