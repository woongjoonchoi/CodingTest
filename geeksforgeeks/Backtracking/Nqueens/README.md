# Nqueens Problem


## Problem Link
[Link](https://www.geeksforgeeks.org/problems/n-queen-problem0315/1)
## Solution Link

[Link](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/)
## Implementation  
 

|Method|Time Complexity|Space Complexity |
|--------------------------------|---------------------------------------------|-----------------------------------|
|No-tail Optimization|$$O(N^{n})$$||
|no-tail optimization 2|$$O(N! * N^{2})$$||
|tail optimization |$$O(N!) $$||
|tail optimization 2|$$O(N!) $$||
## Solutin Improvement
### Solution 큰 틀
반복적인 작업을 통해 Solution을 완성을 해나가므로 , 이는 `increase-and-conquer` 형태의 problem solving 전략을 선택할 수 있다. 즉, recursive 알고리즘을 사용하여 문제를 해결하게 된다.

### 모든 경우의 수를 brute force
모든 경우의 수를 brute force로 탐색을 한다. 체스판이 $$N * N$$ 모양의 grid이므로 총 step의 수는 $$  O(N^{N} )$$ 의 complexity를 가지게 된다

N=10 , Time : 30 min over
### 금지위치를 지정하자.
Queen을 둘 때 마다 갈수 없는 위치를 매번 정해준다. 
#### 같은 row(or col) 상에 두는 것을 피해보자.
> Idea ! 매 step마다 고려해야 하는 grid를 1씩 줄여보자 $$ N \rightarrow K $$   

모든 row(or col)을 조사하는 대신에 이전에 두었던 row(or col)을 기억해두었다가 그 line을 피해가자 . 총 step의 수가 $$ O(N^{N} ) \rightarrow O(N! * N^{2} ) $$ 으로 줄어들게 된다.

N=10 , Time : 19.622090101242065 sec
#### 각 step을 통해서 매번 두면 안되는 곳을 기억한다.
>Idea ! 끝까지 전부 위치시킨 다음에 확인하지 않고 미리 알고리즘을 종료하자.  

queen을 N개 두기전에 미리 알고리즘이 종료되도 되는지 확인해본다.function에 계산한 금지 grid를 복제한 후(deepcopy) variable(parameter)로 넘겨준다. 정확한 steps 수의 변화는 계산하기 어렵지만, worst case에 비해 상당히 진보 된다.  worst case는 $$  O(N! + N^{3} ) $$ 이 된다.

N=10 , Time : 5.024050712585449 sec

#### 매 frame마다 금지 grid를 variable(parameter)로 넘기는게 아니라 function 호출 종료후 복원해준다.

>Idea ! 매번 frame을 만들때마다 grid를 생성하지 않는다.

recursive function 호출시에 생성하는 frame이 최대10개이지만, 알고리즘의 upper bound는 $$ N! $$ 이므로 성능에 상당한 영향을 끼친다. function의 variable에서 grid를 제외해준다. worst case는 $$  O(N! + N^{3} ) $$ 이 된다.

N=10 , Time : 0.16177892684936523 sec

#### 금지 grid의 left diagonal , right diagonal의 규칙을 찾자.

> idea !퀸의 위치와 금지 grid의 위치를  1대다 mapping관계로 생각하는 것이 아닌 1대1 mapping으로 생각해보자.

매번 모든 금지 grid를 전부 저장했는데 , 금지 grid는 직선상에 있으므로 , 규칙성이 존재한다. 이를 이용해주자. 

N=10 , Time : 0.051833152770996094

#### bitmask를 사용해서 저장하자.


>Idea !. bitmask를 사용해서 저장하면 저장공간을 줄일 수 있다.

기존 알고리즘 에서는 diagonal, row(or col)을 체크하기 위해서 $$ 2N-1 $$, $$ N $$ 의 저장공간을 추가적으로 필요했는데, bitmask를 사용하면 int 하나만으로 이를 표현할 수 있다. 
### 금지위치 대신 queen의 위치를 기억
queen의 위치를 매번 기억해준다. 

#### 매번 금지 grid 대신 queen의 위치를 복원
>Idea ! 매번 function을 호출후 금지 grid 대신 queen의 위치를 복원해주자. 

recursive function 호출후 매번 금지 grid를 복원해주었지만, queen의 위치를 복원해준다. 이렇게 되면 매 steps 마다 금지 grid인지 체크하는 대신 이전 queen 의 위치와 새 queen의 위치가 올바른 위치인지 체크해야 한다. 체크시의 complexity는 $$   O(N^{3} ) $$ 이므로 차이가 없지만 복원시의 complexity는 매 steps 마다 $$   O(N^{2} ) \rightarrow O(1) $$ 이 된다.

time : 0.3280527591705322  
생각보다 시간이 줄어들지를 않는다.  그 이유를 고찰해보자면, 금지 영역을 조사하는 알고리즘의 경우 매번 이전 queen과 위치가 겹치는지 확인을 안하는 경우가 있다. 하지만, 이 알고리즘의 경우 이전 queen의 위치만을 저장하기에 매번 이전 queen과 위치를 비교해야만 한다. 
#### 전부 비교를 하지 말자.

>Idea !. 같은 ,row(or col)인지 확인할 때 row값(or col 값)만 비교하는 것 처럼 대각선을 비교할 때 전부 비교하지 말고 , 1대1 mapping 관계로 만들어 주자.

[SpecialStack](https://github.com/woongjoonchoi/CodingTest/tree/main/geeksforgeeks/Stack) 때 처럼 1대 다 mapping되어 있는 것을 1대1 mapping 연결로 변형해준다.grid는 정사각형이기 때문에 , right diagonal 과 left diagonal은 기울기 1인 직선상에 있다. 즉, 일정한  x,y(여기서는 grid point)가 변하더라도 값이 일정하게 유지된다.  right diagonal의 경우 합이 일정하고 , left diagonal의 경우 차이가 일정하다. 이전 queen들의 위치에 대한 right diagonal ,left diagonal의 모든 grid point를 기억하는 것이 아니라 1개의 value만을 기억하게 한다. 이렇게 되면, 체크시의 complexity 는 $$   O(N^{3} ) \rightarrow O(1) $$ 이 된다. 
time : 0.2953176498413086



