while True:
    result = 0
    a = input('Что делаем?(+, -, *, /):')
    try:
        b = float(input('Введите первое число:'))
        c = float(input('Введите второе число:'))
    except ValueError: print('Вы ввели не цифру')
    if a == '+':
        result = b + c
        print (result)
    elif a == '-':
        result = b - c
        print (result)
    elif a == '*':
        result = b * c
        print (result)
    elif a == '/':
        try:
            result = b / c
            print (result)
        except ZeroDivisionError: print('Невозможно выполнить деление на 0')    
    else :
        print('Вы ввели не правильное действие')
 # закрыть или продолжить        
    print('Если хотите продолжить введите Y, если хотите закончить работу введите N')
    d = str(input()) 
    if d == 'Y':
        continue
    elif d == 'N':
        print('программа завершена')
        break
    else :
        print('Вы ввели неизвестное значени, программа завершена')
        break
exit(0)