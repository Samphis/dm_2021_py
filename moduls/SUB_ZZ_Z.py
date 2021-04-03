def SUB_ZZ_Z(num1, num2): #num1 - уменьшаемое, num2 - вычитаемое (!! Добвить return в TRANS_Z_N, иначе функция
    # увелчится раза в два!!)
    if COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 2: #Вычитаемое меньше уменьшаемого
        if POZ_Z_D(num1) == 2:
            if POZ_Z_D(num2) == 2:
                return [0, *SUB_NN_N(TRANS_Z_N(num1), TRANS_Z_N(num2))]
            else:
                return [0, *ADD_NN_N(TRANS_Z_N(num1), ABS_Z_N(num2))]
        else:
            if POZ_Z_D(num2) == 2:
                return[1, *ADD_NN_N(ABS_Z_N(num1), TRANS_Z_N(num2))]
            else:
                return[1, *SUB_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))]
    else:                        # Вычитаемое больше уменьшаемого
        if POZ_Z_D(num2) == 2:
            if POZ_Z_D(num1) == 2:
                return [1, *SUB_NN_N(TRANS_Z_N(num2), TRANS_Z_N(num1))]
            else:
                return [1, *ADD_NN_N(TRANS_Z_N(num2), ABS_Z_N(num1))]
        else:
            if POZ_Z_D(num1) == 2:
                return [0, *ADD_NN_N(ABS_Z_N(num2), TRANS_Z_N(num1))]
            else:
                return [0, *SUB_NN_N(ABS_Z_N(num2), ABS_Z_N(num1))]
