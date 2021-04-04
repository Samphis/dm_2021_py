//Модули: Z-1 -> Z-10
//Формат входных данных: [знак числа(1 - отрицательное, 0 - положительное), количество разрядов; [число]]

import natural_nums

def STR_TO_INT(num):
    if num[0] == '-':
        mas=[1, len(num)-1, [int(i) for i in (num[1::])]]
    else:
        mas=[0, len(num), [int(i) for i in (num)]]
    return mas


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


def MUL_ZM_Z(mas):
    if mas[0] == 1:      #если знак -
        mas[0] = 0       #меняем на +
    else:                #если знак +
        mas[0] = 1       #меняем на -


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


def SUB_ZZ_Z(num1, num2): #num1 - уменьшаемое, num2 - вычитаемое (!! Добвить return в TRANS_Z_N, иначе функция
    # увелчится раза в два!!)
    if COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 2: #Вычитаемое меньше уменьшаемого
        if POZ_Z_D(num1) == 2:
            if POZ_Z_D(num2) == 2:
                return [0, *SUB_NN_N(TRANS_Z_N(num1), TRANS_Z_N(num2))]
            else:
                return [0, *ADD_NN_N(TRANS_Z_N(num1), ABS_Z_N(num2))]
        else:
            if POZ_Z_D(num2) == 2:
                return[1, *ADD_NN_N(ABS_Z_N(num1), TRANS_Z_N(num2))]
            else:
                return[1, *SUB_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))]
    else:                        # Вычитаемое больше уменьшаемого
        if POZ_Z_D(num2) == 2:
            if POZ_Z_D(num1) == 2:
                return [1, *SUB_NN_N(TRANS_Z_N(num2), TRANS_Z_N(num1))]
            else:
                return [1, *ADD_NN_N(TRANS_Z_N(num2), ABS_Z_N(num1))]
        else:
            if POZ_Z_D(num1) == 2:
                return [0, *ADD_NN_N(ABS_Z_N(num2), TRANS_Z_N(num1))]
            else:
                return [0, *SUB_NN_N(ABS_Z_N(num2), ABS_Z_N(num1))]


def MUL_ZZ_Z(num1, num2): #num1, num2 - множители
    if POZ_Z_D(num1) == POZ_Z_D(num2):
        return [0, *natural_nums.MUL_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))]
    else:
        return [1, *natural_nums.MUL_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))]


##DIV_ZZ_Z


##MOD_ZZ_Z
