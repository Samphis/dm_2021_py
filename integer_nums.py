//Модули: Z-1 -> Z-10
//Формат входных данных: [знак числа(1 - отрицательное, 0 - положительное), количество разрядов; [число]]

import natural_nums

def ABS_Z_N(mas1):
    mas1 = mas1[1:]     #берем просто все кроме 1ой цифры
    return mas1

def POZ_Z_D(mas):
    #проверим не равно ли 0 число
    if mas[2][0] == 0:
        return 0
    #если число не ноль, то смотрим на знак
    if mas[0] == 0: #знак +
        return 2
    if mas[0] == 1: #знак -
        return 1


##MUL_ZM_Z


def TRANS_N_Z(mas):
    ##На вход подаётся массив вида [n, A[...]],
    mas = [0]+mas   ##Возвращает массив вида [b, n, A[...]], где b - знак числа,
    return mas      ##записанного в массиве A[...]


def TRANS_Z_N (number):
    if (number[0] == 0):
        number.pop(0)
    else:
        print("Ошибка! Задано отрицательное число")


##ADD_ZZ_Z


##SUB_ZZ_Z


##MUL_ZZ_Z


##DIV_ZZ_Z


##MOD_ZZ_Z
