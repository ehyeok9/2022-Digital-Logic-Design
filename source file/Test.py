from unicodedata import name
from pip import main
from getPI import getPI
from findEPI import findEPI
from remove_EPI_Minterm import remove_EPI_Minterm
from columnDominance import columnDominance
from rowDominance import rowDominance
from petrick import petrick

def test(minterm):
    answer = getPI(minterm)
    print("PI : ", answer, "\n")
    
    cnt = 1
    answer, epi = findEPI(answer, minterm)
    answer = remove_EPI_Minterm(answer, epi)
    print("EPI - ", cnt, " : ", list(epi.keys()))
    print("After Removing EPI : ",answer, "\n")
    while(True):        
        # {'11--': [12, 14], '1--0': [12, 14], '-11-': [6, 14], '--10': [6, 14]} 
        answer, Cdominate_Minterm, Cdominate_pi = columnDominance(answer)
        print("After CD> PI Table : ", answer)
        print("Column Dominance Minterm : ", Cdominate_Minterm)
        print("Column Dominance PI : ", Cdominate_pi, "\n")
        
        answer, Rdominated_PI = rowDominance(answer)
        print("After RD> PI Table : ", answer)
        print("Row Dominance PI : ", Rdominated_PI, "\n"
              )
        if (epi == {} and Cdominate_pi == []):
            sop = petrick(answer)
            print("After Petrick Method : ", sop)
            break
        
        cnt += 1;
        answer, epi = findEPI(answer, minterm)
        answer = remove_EPI_Minterm(answer, epi)
        print("EPI - ", cnt, " : ", list(epi.keys()))
        if (answer == {}):
            break;
        

if __name__ == '__main__':

    test([4, 11, 0, 2, 5, 6, 7, 8, 10, 12, 13, 14, 15])

    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    test([4, 13, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])