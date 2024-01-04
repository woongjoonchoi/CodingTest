#User function Template for python3

# line 30 board[i-(k-steps )][k] - > board[i-(k-steps )][k] == 0
import copy
import time
class Solution:
    def nQueen(self, n):
        # code here
        board = [[0] * n  for _ in range(n) ] 
        # board : store queen's place 
        # 1 , queen 0, not queen
        ans= []

        
        def indexchk(x,y):
            return (x>=0 and x<n and y>=0 and y < n)
            
        def recur_q(steps,sol) :
            if steps == n :
                ans.append(sol)
                return
            for i in range(0,n) :
                
                t= steps-1
                j=1
                # 0104 copy버전과의 차이점은 while을 3개로 분리하여 loop 반복횟수를 줄엿다.
                # 하지만, 그렇게 될경우 flag변수가 필요해질거 같앗기 때문에, 함수로 따로 분리하였다.
                while t>=0 :
                    if indexchk(i,t) and board[i][t] == 1 : break
                    if indexchk(i-j , t ) and board[i-j ][t] == 1:break
                    if indexchk(i+j , t) and board[i+j][t] == 1 :   break
                    j+=1 
                    t-=1
                else :
                    board[i][steps] = 1 
                    recur_q(steps+1,sol+[i+1])
                    board[i][steps] = 0 
        recur_q(0,[])
        return ans
    
start = time.time()
ob =Solution()

ans = ob.nQueen(10)
end= time.time()

print(len(ans))
print('hi')
print("time : {}".format(end-start))