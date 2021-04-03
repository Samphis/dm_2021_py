def MUL_Nk_N (number, deg):
    if deg > 0:
        number[0] += deg
        for i in range (deg):
            number[1].append(0)
    elif deg == 0:
        number = [1, [1]]
    else:
        print("Неверное значение степени")
