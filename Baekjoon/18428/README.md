## BruteForce


### 1 try
- 모든 Teacher,Student 의 위치를 구한다.
- 가능한 모든 장애물의 위치를 다 구한다.
- Brute Force로 해결

### Issue :

***<u>가능한 모든 장애물의 위치를 다 구하는데 고민을 많이 했다.</u>***

#### my solution :

bitmasking으로 가능한 모든 조합을 구한다.

#### common solution:

python 의 itertools를 이용해서 조합을 구한다.

```python
import itertools

itertools.combinations(O,3)
# O에서 3개를 선택하는 모든 경우의 수
```

### 2 try , failed

#### why failed ?

S , T, O 가 같은 라인에 있으면 무조건 감시를 피할 수 있다고 가정

하지만, STO , OST, 같은 case에서는 피할 수 없음

#### 일반화

문제의 조건 :S,T ***<u>사이에</u>*** O가 있어야 하는다

내가 만든 조건 : S,T ,O가 ***<u>같은 line</u>***에 있다.

### 3 try , 2 failed

#### why failed?

***<u>S, T 가 정해졌을 때 , O 3개중 1개만 T,S 사이에 있으면 되는데, 나는 O전부 S,T 사이에 있도록 조건을 설정(코드를 짬)</u>***

#### question

> 정말로 1개의 O가 S,T 사이에 있으면 되는가?

#### answer

1. case1 ex)SOOT : S,T 사이에 O가 여러개 있어야 막을 수 있는가 .? , 1개의 O만 만족해도 나머지는 필요가 없다.
2. case2  S,T 사이에 말고 O가 다른 라인에 있으면 막을 수 있는가? , T와 S는 같은 라인에서만 볼 수 있다.  T,S사이의 라인 말고 다른 라인에서는 볼 수 있는 방법이 없기 다른 라인에 O가 필요 없다.

#### my solution

1개의 O만 만족하지 못해도 감시를 피할 수 없다고 코드함

```
for O in O :
	if :o 가 S,T사이에 없다.
		S가 T로부터 감시를 못피함
		break
	
```



#### solution

모든 O에 대해 조사, 1개라도 만족하면 pass

```
for O in O :
	if :o 가 S,T사이에 없다다.
		pass
	else :
		
		check
	
```

#### 4 try issue

***<u>T가 S를 발견했는지 , 안하는지 어떻게 아는가?(종료조건)</u>***

#### my solution

1. T, S 가 O에 막히면 count를 세줌  
2. 만약, count 가 len(T) * len(S) 이면, 성공 , 아니면 실패

```
for O in O :
	if :o 가 S,T사이에 없다다.
		pass
	else :
		count+=1	
		check
		
if count < len(T) * len(S) :
	print('NO')
else : 
	print('YES')
	
```





## Efficient



BruteForce 보다 시간을 더 줄일 수 없는가 고민

### my idea 1

***<u>되는가 vs 안되는가?  vs O의 위치</u>***

Brute Force 풀이법은 O의 위치를 찾는 것이고 , 문제의 요구사항은 되는가(yES) , 안되는가(NO) 를 묻는다.

***<u>O의 위치를 찾는것 보다 되는가, 안되는가를 찾는 것이 더 빠르다고 생각함.</u>***

### my idea 2

***<u>언제 되는가 vs 언제 안되는가</u>***

언제 되는지를 찾는것 보다 언제 안되는지를 찾는게 빠를 것이다라고 생각

1.  S,T 인접하면 안된다.
2. S 기준으로 동서남북 4방향에서 T가 있나 검색

#### challange

***<u>S기준이면 30개 의 복잡도고, T 기준이면 5개의 복잡도이다.</u>*** 

T를 기준으로 찾는 것이 빠를 것이다 라고 생각



### my idea3

***<u>T, S가 같은 row or 같은column이면 어떻게 할 것인가?</u>***

1. T,S 사이에 전부 표시 : input size n에 따라, O(N)



선점 했다는 표시를 constant로 표시하길 원함(input size에 independent 하게)

(row,row) , (col ,col ) 로 표현하기로 결정.

#### why?

어떤 input size가 들어오더라도 4개의 value로 표현 가능

### challange

***<u>Q1.T의 위치에서 4방향에 대한 check에 대한 조건문을 어떻게 하는가?</u>***

```
dx = [0,0,1,-1]
dy = [1,-1,0,0]        

        if dx[i] <0 or dy[i] < 0 :
            if dx[i] < 0 :
                k = x
            else :
                k= y 
            for m in range(1,k+1) :
                if matrix[x+dx[i] * m][y+dy[i]*m] == 'S' :
                    alloc = [[x+dx[i]*m -dx[i] , x+dx[i]] ,[y+dy[i]*m - dy[i] , y +dy[i] ] ]
                    break
        elif dx[i] >0  or dy[i] >0 :
            if dx[i] > 0 :
                k = x
            else :
                k = y
            for m in range(1,n-k) :
                if matrix[x+dx[i] * m] [y + m * dy[i]] == 'S' :
                    alloc =  [[x+dx[i] , x+dx[i] * m -dx[i]]  , [y+dy[i] , y+dy[i] * m -dy[i] ]]
                    break# matrix[x+dx[i] * m][y+dy[i]*m] = 'C'
```



1. 증가 방향인지 ,감소방향인지 먼저 체크
   1. 증가인지 , 감소인지에 따라서 , 기준점이 달라짐
   2. 반복문의 구간이 달라진다.



***<u>Q2 . 선점 구간을 어떻게 표현하는가</u>***

dx[i] * m -dx[i]   , dy[i] * m -dy[i]으로 표현

dx,dy는 부호에 상관 없이 변화량을 의미한다.

***<u>기준점에서 변화량 만큼 변화시켯을 때 S를 만나는지 체크</u>***



### my idea 4

***<u>선점구간이 유효한지 어떻게 판별하는가?</u>***

ex )STS

인접해 있는 경우 선점할 수가 없다. 하지만, ***<u>로직상 기준점을 제외하면, 변화량이 더 해진 지점에서 변화량을 1개 덜어줘야 한다.</u>***

따라서, ***<u>T의 위치가 선점 위치가 됨으로 오류가 발생한다.</u>*** 이를 조건식으로 처리하엿다.

```
            if alloc[0][0] > alloc[0][1] or alloc[1][0] > alloc[1][1] :
                count_O = -1
                break
```



### my idea 5

***<u>장애물의 선점 구간이 겹칠 때 어떻게 하는가, 안겹치는지 어떻게 하는가?</u>***

장애물의 선점 구간이 겹친다면 어떻게 해야 하는가? 공통 구간을 구해주어야한다.

![image](https://user-images.githubusercontent.com/50165842/149253349-a8a8987e-4cbd-4f9f-9d3c-1f26c1fb5e47.png)

***<u>시작 점의 max 와 , 끝 점의 min을 구해주어서 시작점 max < 시작점  min 인지 확인해 주면 된다</u>***. 구간이 겹치지 않는다면 시작점 max>= 시작점 min이 될  것이다.





```
                if max(alloc[0][0] , x1[0] ) <= min(alloc[0][1] , x1[1])  and \
                    max(alloc[1][0] , y1[0] ) <= min(alloc[1][1] , y1[1]):
```

### my  mistake 1

```
            if not flag and count_O > 0 :
                O.append(alloc)
                count_O-=1
            elif not flag and count_O<0:
                count_O-=1
                break
```

위의 brute force 와 마찬가지로 count_O로 3개 의선점이 끝나고 추가로 더필요 할때 0보다 작게하여 최종 출력시 0보다 작은지를 조건으로 삼았다. 하지만, 위를 보면 `count_O==0` 에 대한 조건이 없다. 