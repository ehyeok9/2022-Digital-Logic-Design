def numof1(answer, last_value):
    lit = {}
    for i in range(last_value+1):
        temp = []
        for j in answer:
            if (j.count("1") == i):
                temp.append(j)
        lit[i] = temp
    return lit