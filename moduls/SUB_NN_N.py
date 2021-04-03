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


def SUB_NN_N(mas1, mas2):
    if COM_NN_D(mas1, mas2) == 2 or COM_NN_D(mas1, mas2) == 0:    #сравниваем два числа, чтобы 1ое было >= 2го
        sum_e = 0
        s = [mas1[0], [0] * (mas1[0])]
        for i in range(-1, -(mas2[0]+1), -1):
            if mas1[1][i] < mas2[1][i]:                         #если цифра в разряде 1го числа меньше цифры 2го, то делаем что и при обычном вычитании
                mas1[1][i] += 10
                mas1[1][i-1] -= 1
            s[1][i] = mas1[1][i]-mas2[1][i]
            if mas1[1][i] >= 10:
                mas1[1][i] -= 10
        for j in range(-mas1[0], -mas2[0]):                     #сохраняем не использованные цифры
            s[1][j] = mas1[1][j]
        i = 0
        r = [mas1[0], [0] * mas1[0]]                            #создаем рез-ий массив, в котором будем избавляться от 0
        while (s[1][i] == 0) and (i < mas1[0]-1):
            r[1] = s[1][i+1:]
            i += 1
        for k in range(mas1[0]):                                #считаем сумму эл-ов, важна только если все 0
            sum_e += s[1][k]
        r[0] = mas1[0] - i                                      #считаем кол-во разрядов нового числа
        if sum_e == 0:
            r[1] = s[1][0:1]
            s = r
        elif r[1][0] != 0:
            s = r
        return s


"думаю можно было бы написать лучше, но как есть D:"


