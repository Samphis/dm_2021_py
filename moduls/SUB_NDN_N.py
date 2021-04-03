def SUB_NDN_N(num1, num2, mult):  # num1 - уменьшаемое, num2 - вычитаемое, mult - множитель вычитаемого (num2)
    MUL_ND_N(mult, num2)
    if COM_NN_D(num1, num2) == 2 or COM_NN_D(num1, num2) == 0:
        return SUB_NN_N(num1, num2)
    else:
        return 'Отрицательный результат'
