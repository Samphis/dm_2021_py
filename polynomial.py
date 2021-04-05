//Модули: P-1 -> P-13
//Формат входных данных: [степень многочлена; [коэффициенты]]

import rational_nums

def STR_TO_POL(coef):


##ADD_PP_P


def SUB_PP_P(minuend, subtrahend):
    mm = minuend[0]
    sm = subtrahend[0]
    result = [sm, []]
    if (sm > mm):
        minuend[0] = sm
        for i in range(sm-mm):
            minuend[1].insert(0, [0, 0, [0]])
    for i in range(sm):
        result[1].append(SUB_QQ_Q(minuend[1][i], subtrahend[1][i]))
    return result


def MUL_PQ_P(mult, polynomial):
    m = polynomial[0]
    for i in range (m+1): #умножаем каждый коэффициент на рациональное число
        polynomial[1][i] = MUL_QQ_Q(polynomial[1][i], mult)


def MUL_Pxk_P(mas, k):
    mas[0] += k
    return mas


def LED_P_Q(mas):
    return mas[1][0]


def DEG_P_N(polynom):
    return polynom[0]


##FAC_P_Q


##MUL_PP_P


##DIV_PP_P


##MOD_PP_P


##GCF_PP_P


def DER_P_P(mas):
    mas[0] -= 1
    for i in range(mas[0]):
        mas[1][i] = mas[1][i] * (mas[0] + 1 - i)
    if len(mas[1]) > mas[0]:
        mas[1].pop()
    return mas


##NMR_P_P
