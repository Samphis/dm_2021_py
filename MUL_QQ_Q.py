def MUL_QQ_Q(num1, num2): #умножение дробей (исп. MUL_NN_N т.к. знаменатель - натуральное)
    return [integer_nums.MUL_ZZ_Z(num1[0], num2[0]), natural_nums.MUL_NN_N(num1[1], num2[1])]
