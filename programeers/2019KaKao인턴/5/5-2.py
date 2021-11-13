from collections import deque

def printMax(arr , n, k ) :

    deq = deque()

    max_ele = 0
    li=[]
    ind = 0

    for i in range(k):

        while deq and arr[i] >= arr[deq[-1]] :
            deq.pop()

        deq.append(i)
    
    min_ele = arr[deq[0]]

    for i in range(k,n) :
        while deq and deq[0] < i-k+1 :
            deq.popleft()
        while deq and arr[deq[-1]] <=arr[i] :
            deq.pop()
        deq.append(i)

        min_ele = min(arr[deq[0]] , min_ele)

    return min_ele

def solution(stones, k):
    answer = 0
    li = []
    s = printMax(stones,len(stones),k)
    return s