def GCF_NN_N(mas1, mas2):                                                   #алгоритм Евклида для поиска НОД
    while NZER_N_B(mas1) == True and NZER_N_B(mas2) == True:
        if COM_NN_D(mas1, mas2) == 2:
            mas1 = MOD_NN_N(mas1, mas2)
        else:
            mas2 = MOD_NN_N(mas2, mas1)
    return ADD_NN_N(mas1, mas2)