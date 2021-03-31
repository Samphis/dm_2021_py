def int_in_rational(sign,num):#sign(0 - положительное, 1 - отрицательное)
    """
    Преобразование целого в дробное
    """
    if sign == 1:#если sign = 1, то замена num на -num
        num = -num
    mas_rational = [num, 1]#массив, состоящий из пары чисел числитель/знаменатель
    return(mas_rational)


