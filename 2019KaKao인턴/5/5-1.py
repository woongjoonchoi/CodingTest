# max_count를 셀게 아니라 , cnt값이 k에 도달하면 멈춘다
# 반복작업
# ->min값을 뺀 다음에  , binary search를 하나 ,
#  처음부터 binary search를 하나 똑같다.

# 가장 숫자가큰 m값을 줄일려 했어야했다.

# binary search를 제대로 이해하지 못했다.

# binary search는 주어진 값의 탐색이 아니라, 특정변수와 그에 해당하는 문제의 값이 mapping되고 , 그 관계가 정렬
# 가능할 때도 적용할 수 있다.
def solution(stones, k):
    answer = 0
    li = []

    max_k = max(stones)
    start = 1
    end = max_k
    max_cnt = 0
    max_in = 0
    while start != end:
        ind = (start+end) //2  + 1
        cnt = 0
        for i ,t in enumerate(stones) :
            if t < ind : 
               cnt+=1
            else :
                cnt = 0
            if cnt == k:
                end = ind-1
                break
        if cnt != k:
            start = ind
    return start

solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)