def MUL_ZZ_Z(num1, num2): #num1, num2 - множители
    if POZ_Z_D(num1) == POZ_Z_D(num2):
        return [0, *natural_nums.MUL_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))]
    else:
        return [1, *natural_nums.MUL_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))]
