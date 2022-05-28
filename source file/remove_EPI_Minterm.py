# column dominance를 시키기 전에 epi가 가지고 있는 minterm들이 nepi가 가지고 있는 minterm에 속해있다면 제거해준다.
def remove_EPI_Minterm(removed_epi, epi):
    removed_epi_minterm = removed_epi
    for epi_key in epi:
        term = epi[epi_key]        
        for nepi_key in removed_epi:
            removed_epi_minterm[nepi_key] = [x for x in removed_epi_minterm[nepi_key] if x not in term]
    
    # 제거 후 NEPI가 가지고 있는 값이 빈 리스트([])인 경우 EPI들에 지배받는 경우(Row Dominance)이므로 먼저 한 번 제거해준다.
    dominated = []
    for key in removed_epi_minterm:
        if (removed_epi_minterm[key] == []):
            dominated.append(key)
    for i in dominated:
        del removed_epi_minterm[i]
    
    return removed_epi_minterm