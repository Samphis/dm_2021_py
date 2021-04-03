#number - массив из двух массивов. Первый массив - числитель, второй - знаменатель
#функция проверяет, является ли число целым
def INT_Q_B (number):
    a = int(''.join((str(i) for i in number[0][1])))
    b = int(''.join((str(i) for i in number[1][1])))
    if a%b == 0:
        return 'да'
    else:
        return 'нет'