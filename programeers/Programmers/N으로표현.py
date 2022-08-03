def solution(N, number):
    answer = -1
    
    dp = [ set() for _ in range(9)]
    
    dp[1].add(N)
    if number in dp[1] :
        answer = 1
        return answer
    for i in range(2,9) :
        for j in range(i,0,-1) :
            for left in dp[j] :
                for right in dp[i-j] :
                    dp[i].add(left + right)
                    dp[i].add(left - right)
                    dp[i].add(left * right)
                    if right != 0 : 
                        dp[i].add(left // right)
        dp[i].add(int(str(1) * i) * N)   
        if number in dp[i] :
            answer = i 
            break
#     for i , k in enumerate(dp) :
        
#         print("index : {}  set : {}".format(i,i))
    return answer