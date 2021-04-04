def SUB_PP_P(minuend, subtrahend):
    mm = minuend[0]
    sm = subtrahend[0]
    result = [sm, []]
    if (sm > mm):
        minuend[0] = sm
        for i in range(sm-mm):
            minuend[1].insert(0, [0, 0, [0]])
    for i in range(sm):
        result[1].append(SUB_QQ_Q(minuend[1][i], subtrahend[1][i]))
    return result
