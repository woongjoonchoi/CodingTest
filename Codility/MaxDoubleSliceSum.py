# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here

    max_prefix_sum=[0] * len(A)
    max_suffix_sum=[0] * len(A)


    for i in range(1,len(A)) :
        max_prefix_sum[i] = max(A[i],A[i]+max_prefix_sum[i-1])
    for i in range(len(A)-2 , -1,-1) :
        max_suffix_sum[i] = max(A[i],A[i]+max_suffix_sum[i+1])

    # print(max_prefix_sum)
    # print(max_suffix_sum)
    max_val = None
    for i in range(1,len(A)-1) :
        if max_val is None : 
            max_val = max(max_prefix_sum[i-1]+max_suffix_sum[i+1] ,
                        max_prefix_sum[i-1] ,
                        max_suffix_sum[i+1])
        max_val= max(max_val,
                        max_prefix_sum[i-1]+max_suffix_sum[i+1]
                        ,max_prefix_sum[i-1] ,
                        max_suffix_sum[i+1])

    # print(max_val)

    if max_val is None : max_val =0
    pass
    return max_val