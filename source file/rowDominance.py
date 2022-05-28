def rowDominance(afterCD):
    afterRD = afterCD
    Rdominated_pi = []
    Interchage = {}
    
    for key1 in afterRD:
        dominate = afterRD[key1]
        for key2 in afterRD:
            dominated = afterRD[key2]
            if (key1 ==key2):
                continue
            remove_dominated = [ x for x in dominate if x not in dominated ]
            dominated = [ x for x in dominated if x not in dominate]
            if (len(remove_dominated) >0 and dominated == []):
                Rdominated_pi.append(key2)
            elif (remove_dominated == [] and dominated == []):
                Interchage[key1] = key2
                
    # Interchange 중복을 제거하기 위한 과정. plus_pi를 Rdominated_pi에 추가할 것이다.
    value = list(Interchage.items())
    plus_pi = []
    rm_pi = []
    for i in range(len(value)):
        if (value[i][0] not in rm_pi):
            plus_pi.append(value[i][0])
            rm_pi.append(value[i][1])
    
    Rdominated_pi = list(set(Rdominated_pi))
    Rdominated_pi += plus_pi
    
    for i in Rdominated_pi:
        del afterRD[i]
    
    return afterRD, Rdominated_pi