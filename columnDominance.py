
def columnDominance(removed_epi_minterm):
    afterCD = removed_epi_minterm
    Cdominate_Minterm = []
    Interchage = {}
    
    # pi의 minterm들을 리스트에 다 저장 후 중복 제거
    mintermValue = []
    for i in removed_epi_minterm:
        mintermValue += removed_epi_minterm[i]
    mintermValue = list(set(mintermValue))
    
    # minterm이 키가 되고 value는 pi가 되는 사전을 생성   
    mintermTable = {}
    for i in mintermValue:
        term = []
        for pi in removed_epi_minterm:
            if (i in removed_epi_minterm[pi]):
                term.append(pi)
        mintermTable[i] = term
      
    for key1 in mintermTable:
        dominate = mintermTable[key1]
        for key2 in mintermTable:
            dominated = mintermTable[key2]
            if (key1 == key2):
                continue
            # 지배하는 minterm에서 지배 당하는 minterm을 제거해줌, 지배 당하는 minterm에서 지배하는 minterm을 제거해준다
            remove_dominated = [x for x in dominate if x not in dominated]
            dominated = [x for x in dominated if x not in dominate]
            # 지배하는 Minterm의 길이가 0 보다 크고 지배 당하는 minterm이 비ㄴ어있으면 지배하는 minterm을 리스트에 추가해준다
            if (len(remove_dominated)> 0 and dominated == []):
                Cdominate_Minterm.append(key1)
            # 지배하는 minterm, 지배당하는 minterm 둘다 비어있을 경우 interchagable하기에 다른 리스트에 추가해준다.
            elif (remove_dominated == [] and dominated == []):
                # 중복을 사전에 방지하지 위해 집합 형식으로 추가해준다.
                Interchage[key1] = key2
                  
    # 중복 제거
    value = list(Interchage.items())
    plus_minterm = []
    remove_minterm = []
    for i in range(len(value)):
        if (value[i][0] not in remove_minterm):
            plus_minterm.append(value[i][0])
            remove_minterm.append(value[i][1])
    
    Cdominate_Minterm = list(set(Cdominate_Minterm))
    Cdominate_Minterm += plus_minterm
    
    # pi의 minterm 중 지배하는 minterm들을 제거해준다
    for i in Cdominate_Minterm:
        for key in afterCD:
            term = afterCD[key]
            if (i in term):
                del term[term.index(i)]
                afterCD[key] = term
    
    # 지배하는 minterm을 제거해준 뒤 minterm을 가지지 않는 pi를 제거해준다.
    Cdominate_pi = []
    for key in afterCD:
        if (afterCD[key] == []):
            Cdominate_pi.append(key)
    for i in Cdominate_pi:
        del afterCD[i]

    return afterCD, Cdominate_Minterm, Cdominate_pi