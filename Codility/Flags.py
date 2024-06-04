# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(A):
    # Implement your solution here

    if len(A) <  3 : return 0
    ans = 1
    peak_ind = []
    for i in range(1,len(A)-1) :
        if A[i-1] <A[i] and A[i] > A[i+1] :
            peak_ind.append(i)

    # print(peak_ind)
    if len(peak_ind) < 1 : return 0
    if len(peak_ind) == 1 : return 1
    max_k = math.floor((1+  (1+4 * (peak_ind[-1] - peak_ind[0])  )**(1/2)  )/2  )


    L=0
    R = max_k


    while L<= R :
        # print(f'L  :{L}  R: {R}  m :{math.floor((L+R)/2)}')
        m = math.floor((L+R)/2)
        count =0
        temp_val =0
        for i in range(1,len(peak_ind)) : 
            if temp_val < m : 
                temp_val += peak_ind[i] -peak_ind[i-1]
                # print(f'temp_val {temp_val}')
            
            if temp_val >=m :
                count += 1
                temp_val = 0
        if count >= m -1: 
            L = m + 1
        else : 
            R = m-1
        # print(f'count :{count}')

    count =0
    temp_val =0
    li = [max(L,R) ,min(L,R)]
    for m in li : 
        count=0
        for i in range(1,len(peak_ind)) : 
            if temp_val < m : 
                temp_val += peak_ind[i] -peak_ind[i-1]
            if temp_val >=m :
                count += 1
                temp_val = 0

        # print(f'm : {m} count  :{count}' )
        if count >= m-1 :
            ans = m 
            break
    
    # print(L)
    # print(R)
        
    return ans
        # print((1+  (1+4 * len(peak_ind)  )**(1/2)  )/2  )
    # print(max_k)
    pass