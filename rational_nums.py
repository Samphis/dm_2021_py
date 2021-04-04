//Модули: Q-1 -> Q-8
//Формат входных данных: [[числитель]; [знаменатель]]

import natural_nums
import integer_nums

##RED_Q_Q


def INT_Q_B (number):
    a = int(''.join((str(i) for i in number[0][1])))
    b = int(''.join((str(i) for i in number[1][1])))
    if a%b == 0:
        return 'да'
    else:
        return 'нет'


def TRANS_Z_Q(sign,mas):#sign(0 - положительное, 1 - отрицательное)
                              #mas - массив вида [n, A[...]]
    if sign == 1:#если sign = 1, то знаменатель отрицательный, если =0, положительный
        mas_rational = [mas, -1]#массив, состоящий из пары чисел числитель/знаменатель
    else:
        mas_rational = [mas, 1]
    return(mas_rational)


def TRANS_Q_Z(mas):
    if mas[1][0] == 1:
        if mas[0][0] == "-":
            new_mas = [1, len(mas[0])-1, mas[0][1:]]
        else:
            new_mas = [0, len(mas[0])-1, mas[0][1:]]
        return new_mas
    else:
        return mas


##ADD_QQ_Q


##SUB_QQ_Q


def MUL_QQ_Q(num1, num2): #умножение дробей (исп. MUL_NN_N т.к. знаменатель - натуральное)
    return [integer_nums.MUL_ZZ_Z(num1[0], num2[0]), natural_nums.MUL_NN_N(num1[1], num2[1])]


##DIV_QQ_Q
