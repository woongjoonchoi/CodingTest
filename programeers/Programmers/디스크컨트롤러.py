import heapq


# 1. heap key를 실제 대기시간-> 소요시간  
#  잘못 쓴 이유 : 문제 정의할 때 임의의 수 a_k를 아무생각없이 정의함


#2 . heap 이 알아서 정렬이 되어있을거라 착각
#  heap에 대해 정리를 잘하자

def solution(jobs):
    
    answer = 0
    base_time= -1
    length = len(jobs)
    
    
    
    
    for i in range(len(jobs)) :
        jobs[i].append(jobs[i][1])
    
    heapq.heapify(jobs)
    
    print(jobs)
#     0 : base_time  , 1: 소요시간, 2 : 실제 대기시간
    while jobs :
        base_time , con_time , ac_time  = heapq.heappop(jobs)
        answer += ac_time
        base_time += con_time
        for i in range(len(jobs)) : 
            req = jobs[i][0]            
            if req <= base_time :
                jobs[i][2] += (base_time-req)
                jobs[i][0] = base_time
        heapq.heapify(jobs)
        # print(jobs)
        
    # print(answer)
    
    return answer//length 

