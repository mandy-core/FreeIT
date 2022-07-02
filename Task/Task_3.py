import math
from stat import FILE_ATTRIBUTE_ENCRYPTED
import numpy as np

#///// 3.1
print('Hello world')

#///// 3.2
user = input('Your name: ')
print(f'Hello, {user}')

#///// 3.3
a = 'Hi, I am a string variable'
b = 100
print(a + str(b))

#///// 3.4
Y = math.factorial(100)
print(Y)

#///// 3.5
tup = tuple(i for i in range(0, 102, 2))
print(tup)

#///// 3.6
num1 = list(np.array(tup)**2)
print(num1)

#///// 3.7
type_of_file =  'sounds/lofi/chillstep.wav'
print(type_of_file)
new_type = type_of_file.replace ('sounds', 'midi')
print(new_type)
print(new_type[10:])

#///// 3.8
a_lst = [1, 1, 2, 3, 5, 8, 10, 10]
print(list(set(a_lst)))

#///// 3.9
b_lst = list(np.array(a_lst)+1)
print(b_lst)

#///// 3.10
print('Python is the most popular programming language' .count('p'))

#///// 3.11

lst_y = [0, 2, 3, 4] 
lst_x = [2, 2, 5]
lst_z = lst_y + lst_x
print(list(set(lst_z)))
