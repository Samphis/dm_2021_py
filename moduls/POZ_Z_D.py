def sign(mas):
    #проверим не равно ли 0 число
    if mas[2][0] == 0:
        return 0
    #если число не ноль, то смотрим на знак
    if mas[0] == 0: #знак +
        return 2
    if mas[0] == 1: #знак -
        return 1