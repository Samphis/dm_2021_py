#функция умножает два натуральных числа - a и b
def MUL_NN_N(a, b):
    s = [1, [0]]
    c = [1, [0]]
    for i in range(0, len(b[1])):
        c[0] = a[0]
        c[1] = a[1].copy()
        MUL_ND_N(b[1][len(b[1])-1-i], c)
        MUL_Nk_N(c, i)
        s = ADD_NN_N(s, c)
    return s