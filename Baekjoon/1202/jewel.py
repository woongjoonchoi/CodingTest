import heapq
import sys
N ,K = list(map(int,input().split()))
jewel=[]
bag=[]
for _ in range(N):
    jewel.append(list(map(int,sys.stdin.readline().split())))
    
for _ in range(K):
    bag.append(int(sys.stdin.readline()))
    
jewel.sort()
bag.sort()
# print(j)

pq = []
# print(bag)
i = 0
j = 0
# ans_list = []
ans =0
while i < N and j<K :
    if jewel[i][0] <= bag[j] :
        heapq.heappush(pq,(-jewel[i][1] , jewel[i][0]))
        i+=1
    else :
        if pq :
            popped= heapq.heappop(pq)
            # print(f'bag {bag[j]}   jewel : value {-popped[0]} jewel gram :{popped[1]}')
            ans += -popped[0]
        j+=1
    # print(f'i : {i}  j: {j}')

while j< K and pq :
    popped= heapq.heappop(pq)
    # print(f'bag {bag[j]}   jewel : value {-popped[0]} jewel gram :{popped[1]}')
    ans += -popped[0]
    j+=1
    #  heapq.heappush()
# print(f'ans  : {ans}')
print(ans)