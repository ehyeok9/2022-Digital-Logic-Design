from numof1 import numof1
from findPI import findPI
from sorting import sorting

def getPI(minterm):
    answer = []
    result = []
    for i in range(2, len(minterm)):
        temp = bin(minterm[i]).replace("0b", "")
        if (len(temp) != minterm[0]):
            temp = (minterm[0]- len(temp))*"0" + temp
        answer.append(temp)
    
    last_value = minterm[0]
    answer = numof1(answer, last_value)
    answer, pi = findPI(answer, 0, last_value)
    result.append(pi)
    
    while(1):
        if (answer == {}):
            break;
        key_value = list(answer.keys())
        first_value = key_value[0]
        last_value = key_value[-1]
        answer, pi = findPI(answer, first_value, last_value)    
        result.append(pi)
        
    answer = []
    for i in range(len(result)):
        for j in range(len(result[i])):
            answer.append(result[i][j])
            
    answer = list(set(answer))
    answer = sorting(answer)
    return answer