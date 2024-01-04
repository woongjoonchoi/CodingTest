#User function Template for python3

# line 30 board[i-(k-steps )][k] - > board[i-(k-steps )][k] == 0
import copy
import time
class Solution:
    def nQueen(self, n):
        # code here
        board = [[0] * n  for _ in range(n) ] 
        ans= []
        def indexchk(x):
            
            return (x>=0 and x<n)
            
        def recur_q(steps,sol) :
            if steps == n :
                ans.append(sol)
                return
            for i in range(0,n) :
                # 
                
                # 이부분이 성능차이가 나는 부분이다.
                if board[i][steps ] == 1 : continue  
                diff = []
                for k in range(steps+1,n) :
                    if board[i][k] == 0 :
                        board[i][k] = 1
                        diff.append((i,k))
                    if indexchk(i+(k-steps )) and board[i+(k-steps ) ][k] == 0:
                        board[i+(k-steps ) ][k] =1
                        diff.append(( i+(k-steps ) , k))
                    
                    if indexchk(i-(k-steps )) and board[i-(k-steps )][k] == 0 :    
                        board[i-(k-steps )][k] = 1
                        diff.append(  (i-(k-steps ) , k )  )
                
                recur_q(steps+1,sol+[i+1])
                for x,y in diff :
                    board[x][y] = 0
        recur_q(0,[])
        return ans
    
start = time.time()
ob =Solution()

ans = ob.nQueen(10)
end= time.time()

print(len(ans))
print("time : {}".format(end-start))