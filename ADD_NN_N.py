def COM_NN_D(mas1, mas2):
    if mas1[0] > mas2[0]:
        return 2
    if mas1[0] < mas2[0]:
        return 1
    if mas1[0] == mas2[0]:
        k = mas1[0]
        for i in range(k):
            if mas1[1][i] > mas2[1][i]:
                return 2
            if mas1[1][i] < mas2[1][i]:
                return 1

        return 0


def ADD_NN_N(mas1, mas2):
    n=0
    s=[]
    if mas1[0] == mas2[0]:                          #если кол-во разрядов одинаковое, то на всякий случай
        s = [mas1[0], [0] * (mas1[0] + 1)]          #cоздаем массив на 1 эл-нт больше максимального
        for i in range(-1, -(mas1[0] + 1), -1):
            s[1][i] = mas1[1][i] + mas2[1][i]
        n = mas1[0]
    elif COM_NN_D(mas1, mas2) == 2:
        s = [mas1[0], [0] * (mas1[0]+1)]
        for j in range(-mas1[0], -mas2[0]):         #элементы, которые не меняются сохраняем
            s[1][j] = mas1[1][j]
        for i in range(-1, -(mas2[0]+1), -1):
            s[1][i] = mas1[1][i]+mas2[1][i]
        n = mas1[0]
    elif COM_NN_D(mas1, mas2) == 1:
        s = [mas2[0], [0] * (mas2[0] + 1)]
        for j in range(-mas2[0], -mas1[0]):         #элементы, которые не меняются сохраняем
            s[1][j] = mas2[1][j]
        for i in range(-1, -(mas1[0] + 1), -1):
            s[1][i] = mas1[1][i] + mas2[1][i]
        n = mas2[0]

    for j in range(-1, -(n + 1), -1):                #проверяем если эл-ты массива >10 и приводим число к нормальному виду
        if s[1][j] >= 10:
            s[1][j] = s[1][j] - 10
            s[1][j - 1] = s[1][j - 1] + 1

    if s[1][0] == 0:                                #если лишний разряд не понадобился, то перезаписываем
        d = [n, [0] * n]
        for i in range(n):
            d[1][i] = s[1][i+1]
        s = d
    else:
        s[0] += 1
    return s
"думаю можно было бы написать лучше, но как есть D:"
