# :computer: 2022DATALOGICDESIGN :computer:
> ### kookmin University 논리 회로 설계 - 도전 과제 
> ### Column Dominance, Row Dominance ,Petrick method

## :ballot_box_with_check: Project Goal
Minterm이 주어졌을 때, 해당하는 Minterm을 최적화하기 위한 CD, RD, PM을 구현하는 것

## :clock130: Period
2022/04/28 (Thursday) ~ 2020/11/28 (Sunday)

## :file_folder: Code Description
:one: remove_EPI_Minterm.py
> Column Dominance를 하기 전, **EPI가 가지고 있는 minterm**들이 NEPI가 가지고 있는 minterm에 속해있다면 **제거**해준다.
> 
> 제거 후 NEPI가 가지고 있는 값이 **빈 리스트**인 경우는 EPI들에게 **지배받는 경우(Row Dominance)**이므로 먼저 제거해준다.
> 
> EPI의 minterm이 제거 된 **PI 테이블**을 리턴한다.

:two: columnDominance.py
> PI Table을 인자로 받아서, **minterm이 row**가 되고 **PI가 column**이 되는 **테이블을 생성**한다.
> 
> 각 minterm의 value(=PI)를 비교해서 **지배하는 minterm** 또는 **서로를 지배하는(Interchagable)** minterm을 찾아준다.
> 
> **Interchagable한 minterm**의 경우에는 두 minterm 중 하나를 **임의로** 선택해서 삭제할 minterm 리스트에 추가한다.
> 
> **지배하는 minterm**을 인자로 받은 PI Table에서 **삭제**한다.
> 
> PI Table에서 PI가 가지고 있는 **Minterm 값이 없다면** PI를 Table에서 **제거**해준다.
> 
> **수정된 PI Table, 지배하는 Minterm의 리스트, 제거된 PI의 리스트**를 리턴한다.

:three: rowDominance.py
> PI Table을 인자로 받아서, 각 PI의 **minterm을 비교**한다.
> 
> 비교를 통해 **지배받는 PI**를 또는 **서로를 지배하는(Interchagable)** PI을 찾아준다.
> 
> **Interchagable한 minterm**의 경우에는 두 minterm 중 하나를 **임의로** 선택해서 삭제할 minterm 리스트에 추가한다.


:four: petrick.py
> PI에 해당하는 minterm이 하나인 경우, 다음 findEPI에서 검출되어야 할 **EPI**이므로 Petrick Method에서 **제외**시켜준다.
> 
> **minterm이 row**가 되고 **PI가 column**이 되는 테이블을 생성한다.
> 
> 테이블 루프를 통해, 아래 **두가지 조건**을 만족하면 minterm에 해당하는 **PI를 SOP에 추가**한다.
> 
> 1. **이전 반복**에 의해 **minterm 값**이 **삭제**되지 않아야 한다.
> 2. **해당하는 minterm**이 가지고 있는 **모든 PI**가 **이전 반복**에 의해 **선택**되지 않아야 한다.
> 
> **최적화된 논리합(=SOP)**를 리턴한다. 

## :clipboard: System Structure
:repeat: Test.py

:arrow_down: (1) PI 테이블에서 모든 PI를 찾는다.

:arrow_down: (2) 테이블에서 EPI를 찾고 제거한다.  
    :arrow_right: 더이상  NEPI가 없으면 QUIT

:arrow_down: (3) Column Dominance를 적용한다.

:arrow_down: (4) Row Dominance를 적용한다.

:arrow_down: (5) (2)와 (3)을 통해 어떠한 최적화가 되었다면 **(2)로**, 되지 않았다면 **Petrick method**를 적용한다.


## :page_with_curl: Description of the results

#### 1번 테스트 케이스 : [4, 11, 0, 2, 5, 6, 7, 8, 10, 12, 13, 14, 15]

:one: Column Dominance를 하기 전, EPI('-0-0', '-1-1')와 EPI에 속해있는 minterm(0,2,8,10 / 5,7,13,15)을 제거해준다.

![title](/img/TEST1-ARE.png)

:two: Column Dominance : 표를 보면 minterm 14가 minterm 6,12를 지배하므로 minterm 14를 제거한다. 

![title](/img/CD-TABLE.png)

![title](/img/TEST1-CD.png)

:three: Row Dominance : ‘11--’과 ‘1–0’, ‘-11-’과 ‘--10’이 서로를 지배하는 관계(Interchagable)이므로 임의로 제거한다

![title](/img/RD-TABLE.png)

![title](/img/TEST1-RD.png)

:repeat: Test.py 출력
![title](/img/TEST1-TOTALRESULT.png)

#### 2번 테스트 케이스 : [4, 13, 0, 2, 3, 4, 5, 6 ,7 ,8, 9, 10, 11, 12, 13]

:one: Column Dominance : 2 → 3, 4 → 5, 6 →7, 8→ 9, 10 → 11, 12 → 13 이렇게 지배하는 - 지배당하는 구조가 형성된다. 지배하는 [ 2, 4, 6, 8, 10, 12 ] minterm을 제거한다.

![title](/img/CD-TABLE2.png)

![title](/img/TEST2-CD.png)

:two: Row Dominance :  ‘--00’, ‘0–0’, ‘-0-0’이 서로를 지배하는 관계(Interchagable)이다. 임의로 하나의 pi만 남긴다.

![title](/img/RD-TABLE2.png)

![title](/img/TEST2-RD.png)

:three: Petrick Method  :  minterm 0에 해당하는 pi는 다음 단계에서 찾아야 할 epi 이므로 제외시켜준다. 나머지 minterm들을 통해 최소 논리곱의 합(SOP)를 얻는다.

![title](/img/PETRCIK-TABLE.png)

![title](/img/TEST2-P.png)

:repeat: Test.py 출력
![title](/img/TEST2-TOTALRESULT.png)