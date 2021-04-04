##Модули: N-1 -> N-14
##Формат входных данных: [количество разрядов; [число]]


def COM_NN_D(mas1, mas2):
    if mas1[0] > mas2[0]:   #если в 1-ом числе разрядов больше, то оно больше 2-ого числа
        return 2
    if mas1[0] < mas2[0]:   #если в 1-ом числе разрядов меньше, то оно меньше 2-ого числа
        return 1
    if mas1[0] == mas2[0]:
        n = mas1[0]
        for i in range(n):
            if mas1[1][i] > mas2[1][i]:
                return 2
            if mas1[1][i] < mas2[1][i]:
                return 1
        return 0    #если весь цикл прошел, и функция не вернула значения, то числа равны и мы возвращаем 0


def NZER_N_B(mas):
    check = True    #Возвращаемое значение функции
    if mas[1][0] == 0:
        check = False
    return check


##ADD_1N_N


def ADD_NN_N(mas1, mas2):
    if mas1[0] == mas2[0]:                              #если кол-во разрядов одинаковое, то на всякий случай
        s = [mas1[0], [0] * (mas1[0] + 1)]              #cоздаем массив на 1 эл-нт больше максимального
        for i in range(-1, -(mas1[0] + 1), -1):
            s[1][i] = mas1[1][i] + mas2[1][i]
            n = mas1[0]

    elif COM_NN_D(mas1, mas2) == 2:
        s = [mas1[0], [0] * (mas1[0]+1)]
        for j in range(-mas1[0], -(mas1[0]-mas2[0])):   #элементы, которые не меняются сохраняем
            s[1][j] = mas1[1][j]
        for i in range(-1, -(mas2[0]+1), -1):
            s[1][i] = mas1[1][i]+mas2[1][i]
            n = mas1[0]

    elif COM_NN_D(mas1, mas2) == 1:
        s = [mas2[0], [0] * (mas2[0] + 1)]
        for j in range(-mas2[0], -(mas2[0] - mas1[0])): #элементы, которые не меняются сохраняем
            s[1][j] = mas2[1][j]
        for i in range(-1, -(mas1[0] + 1), -1):
            s[1][i] = mas1[1][i] + mas2[1][i]
            n = mas2[0]

    for j in range(-1, -(n + 1), -1):           #проверяем если эл-ты массива >10 и приводим число
        if s[1][j] >= 10:                       #к нормальному виду
            s[1][j] = s[1][j] - 10
            s[1][j - 1] = s[1][j - 1] + 1

    if s[1][0] == 0:                            #если лишний разряд не понадобился, то перезаписываем
        d = [n, [0] * n]                        #все в новый массив
        for i in range(n):
            d[1][i] = s[1][i+1]
        s = d
    else:
        s[0] += 1
    return s


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


def MUL_ND_N(multiplier, number):
    if multiplier == 0:
        number[:] = [0, [0]]
    elif 10 > multiplier > 0:
        overflow = number[1][len(number[1]) - 1] * multiplier // 10  # variable storing value left to add to the next digit
        number[1][len(number[1]) - 1] = number[1][len(number[1]) - 1] * multiplier % 10
        for i in range(len(number[1]) - 2, -1, -1):
            tmp = number[1][i]
            number[1][i] = (number[1][i] * multiplier + overflow) % 10
            overflow = (tmp * multiplier + overflow) // 10
        if overflow > 0:
            number[1].insert(0, overflow)
            number[0] += 1
    else:
        print("Wrong multiplier value!")


def MUL_Nk_N (number, deg): #number - число, deg - степень
    if deg > 0: 
        number[0] += deg
        for i in range (deg):
            number[1].append(0)
    elif deg < 0:
        print("Неверное значение степени")


def MUL_NN_N(a, b): #a и b - множители
    s = [1, [0]]
    c = [1, [0]]
    for i in range(0, len(b[1])):
        c[0] = a[0]
        c[1] = a[1].copy()
        MUL_ND_N(b[1][len(b[1])-1-i], c)
        MUL_Nk_N(c, i)
        s = ADD_NN_N(s, c)
    return s


def SUB_NDN_N(num1, num2, mult):  # num1 - уменьшаемое, num2 - вычитаемое, mult - множитель вычитаемого (num2)
    MUL_ND_N(mult, num2)
    if COM_NN_D(num1, num2) == 2 or COM_NN_D(num1, num2) == 0:
        return SUB_NN_N(num1, num2)
    else:
        return 'Отрицательный результат'


##DIV_NN_Dk


##DIV_NN_N


##MOD_NN_N


##GCF_NN_N


##LCM_NN_N
