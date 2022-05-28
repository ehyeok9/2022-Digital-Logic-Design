def findPI(answer, first_value, last_value):
    result = {}
    pi = []

    for i in range(first_value, last_value+1):
        val = answer[i]
        for j in val:
            pi.append(j)

    for i in range(first_value, last_value):
        prev = answer[i]
        daem = answer[i+1]                        
        # if (len(prev) == 0 or len(daem) == 0):
        #     continue
        temp_lit = []
                
        for j in range(len(prev)):
            comp = prev[j]
            
            for k in range(len(daem)):
                comped = daem[k]
                # if (comp.find('-') != comped.find('-')):
                #     continue
                hd = 0
                value = ""                
                for p in range(len(comp)):
                    if (comp[p] == comped[p]):
                        value += comp[p]
                    else:
                        if (hd == 0):
                            hd += 1;
                            value += '-'
                        else:
                            hd = -1
                            break                           
                if (hd == 1):
                    temp_lit.append(value)
                    if (comp in pi):
                        pi.remove(comp)
                    if (comped in pi):
                        pi.remove(comped)

        result[i] = list(set(temp_lit))  
    return result, pi