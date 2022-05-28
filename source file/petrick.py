def petrick(answer):
    # pi에 해당하는 minterm이 하나인 경우, 이는 epi이므로 제외시켜준다.
    epi = []
    for key in answer:
        if (len(answer[key]) == 1):
            epi.append(key)
    print("EPI : ", epi, "\n")
    for i in epi:
        del answer[i]
        
    minterm = []
    for key in answer:
        minterm += answer[key]
    minterm = list(set(minterm))
    
    # minterm(row)- pi(column) 형식의 테이블 생성
    mintermTable = {}
    for i in minterm:
        term = []
        for pi in answer:
            if (i in answer[pi]):
                term.append(pi)
        mintermTable[i] = term
    
    #
    minterm = set(minterm)
    sop = []
    
    for key in mintermTable:
        # 만약 이전 반복에 의해 minterm이 포함 되었다면 continue
        if (key not in minterm):
            continue
        cnt = 0
        flag = False
        choice = mintermTable[key][cnt]
        choice_minterm = set(answer[choice])
        # 이전 반복에 이미 선택된 pi이면 해당 minterm을 포함하는 다른 pi를 순차적으로 탐색한다.
        if (choice in sop):
            choice_length = len(mintermTable)
            while(True):
                cnt += 1
                choice = mintermTable[key][cnt]
                # 모든 pi가 선택되었으면 flag 변수 값을 참으로 만든 후 break and continue
                if (cnt == choice_length-1):
                    flag = True
                    break
                # 해당하는 pi가 선택된 pi가 아니라면 이 pi를 선택한다.
                if (choice not in sop):
                    break
        if (flag):
            continue
        # 선택 된 pi를 sop 리스트에 추가한다. 그리고 선택된 pi가 포함하는 minterm을 제거한다.
        sop.append(choice)
        minterm -= choice_minterm
        
    return sop