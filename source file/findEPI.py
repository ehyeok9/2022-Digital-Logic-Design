def findEPI(pi, minterm):
    dic = {}
    # pi들을 combined 갯수에 따라 0~2^num의 값을 2진수로 만들어 val에 넣어줌 => combined의 갯수에 따라 pi가 나타낼 수 있는 값의 경우의 수가 달라지기에 combinde=0 -> 1 combined=2 -> 4
    for i in pi:
        val = []                
        num = i.count("-")
        for j in range(pow(2, num)):
            val.append(bin(j))
        
        # val에 넣어진 값들을 "00" "01" "10" "11" 과 같이 원하는 형태로 만들어줌
        answer = []
        for j in range(len(val)):
            temp = val[j].replace("0b", "")
            if (len(temp) != num):
                temp = (num- len(temp))*"0" + temp
            answer.append(temp)   
        
        # pi당 나타낼 수 있는 경우의 수를 모두 10진수로 바꾸어 result에 넣어준다 
        result = []
        for j in range(len(answer)):
            tmp = ""
            idx = 0
            for k in range(len(i)):
                if (i[k] == "-"):
                    tmp += answer[j][idx]
                    idx += 1
                else:
                    tmp += i[k]
            result.append(int(tmp,2))
        dic[i] = result
    keys = []
    for key in dic:
        keys.append(key)

    epi = {}
    
    # 선택된 pi를 제외한 모든 pi의 minterm을 초기 minterm에서 삭제시켜줌. 이 과정 후에 남아 있는 minterm이 있다면 그것은 epi가 된다.
    for i in range(len(keys)):
        term = minterm
        for j in range(len(keys)):
            if (i == j):
                continue
            term = [ x for x in term if x not in dic[keys[j]]]
        if (term != []):
            # 삭제된 것 중 원래 minterm이 아닌 것들이 남았을 때 epi가 확정 됨
            u = [ x for x in term if x not in dic[keys[i]]]
            if (len(u) != len(term)):
                epi[keys[i]] = dic[keys[i]]
                
    # dictionary에서 epi 제거
    for key in epi:
        del dic[key]
    
    # return =  발견한 epi를 제거한 answer랑 epi를 리턴한다
    return dic, epi