def MUL_PQ_P(mult, polynomial):
    m = polynomial[0]
    for i in range (m+1):
        polynomial[1][i] = MUL_QQ_Q(polynomial[1][i], mult)
