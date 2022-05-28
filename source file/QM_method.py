from getPI import getPI
from findEPI import findEPI
from remove_EPI_Minterm import remove_EPI_Minterm
from columnDominance import columnDominance
from rowDominance import rowDominance


def solution(minterm):
    PI = getPI(minterm)
    print("PI : ", PI)
    
    removed_epi, EPI = findEPI(PI, minterm)
    print("EPI : ",  EPI)
    print("Removed EPI : ", removed_epi)    
    
    removed_epi_minterm = remove_EPI_Minterm(removed_epi, EPI)
    print("Removed EPI's Minterm : ", removed_epi_minterm)
    
    afterCD, Cdominate_Minterm, Cdominate_pi = columnDominance(removed_epi_minterm)
    print("Column Dominance Minterm : ", Cdominate_Minterm)
    print("Column Dominance PI : ", Cdominate_pi)
    
    afterRD, Rdominated_PI = rowDominance(afterCD)
    print("Row Dominance PI : ", Rdominated_PI)


if __name__ == '__main__':   
    
    solution([4, 11, 0, 2, 5, 6, 7, 8, 10, 12, 13, 14, 15])