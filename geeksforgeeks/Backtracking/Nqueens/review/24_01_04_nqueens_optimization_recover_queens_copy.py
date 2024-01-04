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
        def issafe(i,steps) :
            t = steps -1
            j=1
            while t >=0 :
                if board[i][t] == 1: return False
                t-=1
            t = steps-1
            j=i-1
            while t >=0 and j>=0 :
                if board[j][t] == 1 : return False
                t-=1
                j-=1
            t = steps-1
            j = i+1
            while t>=0  and j<n :
                if board[j][t] == 1 :  return False
                t-=1
                j+=1
            return True
                    
        def recur_q(steps,sol) :
            if steps == n :
                ans.append(sol)
                return
            for i in range(0,n) :
                
                if not issafe(i,steps) : pass
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