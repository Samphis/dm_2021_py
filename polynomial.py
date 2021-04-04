//Модули: P-1 -> P-13
//Формат входных данных: [степень многочлена; [коэффициенты]]

import rational_nums

##ADD_PP_P


##SUB_PP_P


##MUL_PQ_P

def MUL_Pxk_P(mas, k):
    return mas[0] + k


##LED_P_Q


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
    return(mas) 


##NMR_P_P
