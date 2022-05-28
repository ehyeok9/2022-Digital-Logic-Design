def sorting(answer):
    temp = []
    for i in range(len(answer)):
        tmp = answer[i].replace("-", "2")
        temp.append((i,tmp))
    temp.sort(key=lambda x:x[1])
    result = []
    for i in range(len(temp)):
        idx = temp[i][0]
        result.append(answer[idx])
    return result