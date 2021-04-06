def DIV_NN_N(mas1, mas2):
    num1 = 0
    num2 = 0
    count = 0
    result = [1, []]
    for i in range(mas1[0]):
        num1 = num1 + mas1[1][i] * (10 ** (mas1[0] - i - 1))
    for i in range(mas2[0]):
        num2 = num2 + mas2[1][i] * (10 ** (mas2[0] - i - 1)) #тут код Сани, вообще без изменений, см. его комы
    if COM_NN_D(mas1, mas2) == 1:
        quot = num2 // num1
        ost = quot % 10                                      #сэйвим последнию цифру числа, т.к она не попадет в цикл
        while quot // 10 != 0:
            count += 1
            quot = quot // 10
            result[1].append(quot)
        result[1].append(ost)
        result[0] = count + 1
    else:
        quot = num1 // num2
        ost = quot % 10                                     #сэйвим последнию цифру числа, т.к она не попадет в цикл
        while quot // 10 != 0:
            count += 1
            quot = quot // 10
            result[1].append(quot)
        result[1].append(ost)
        result[0] = count + 1                               #т.к count не учитывает наш последний разряд, то увеличиваем его на 1
    return result
