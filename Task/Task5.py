g = True
while g == True:
    result = 0
    a = input('Что делаем?(+, -, *, /):')
    if a == '+':
        try:
            b = float(input('Первое слагаемое:'))
            c = float(input('Второе слагаемое:'))
            result = b + c
            print (result)
        except ValueError: print('Вы ввели не цифру')
        
    elif a == '-':
        try:
            b = float(input('Уменьшаемое:'))
            c = float(input('Вычитаемое:'))
            result = b - c
            print (result)
        except ValueError: print('Вы ввели не цифру')
    elif a == '*':
        try:
            b = float(input('Первый множитель'))
            c = float(input('Второй множитель'))
            result = b * c
            print (result)
        except ValueError: print('Вы ввели не цифру')
    elif a == '/':
        try:
            b = float(input('Делимое:'))
            c = float(input('Делитель'))
            result = b / c
            print (result)
        except ZeroDivisionError: print('Невозможно выполнить деление на 0')
        except ValueError: print('Вы ввели не цифру')
    else :
        print('Вы ввели не правильное действие')

    print('Если хотите продолжить введите Y, если хотите закончить работу введите N')
    d = str(input()) 
    if d == str('Y'):
        g = True
    elif d == str('N'):
        print('программа завершена')
        break
    else :
        print('Вы ввели неизвестное значени, программа завершена')
        break
exit(0)
