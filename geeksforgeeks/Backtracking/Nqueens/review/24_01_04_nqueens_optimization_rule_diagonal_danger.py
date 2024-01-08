#User function Template for python3

# line 30 board[i-(k-steps )][k] - > board[i-(k-steps )][k] == 0
import copy
import time
class Solution:
    def nQueen(self, n):
        # code here


        ans= []
        left_diagonal = [False] * (2*n-1)
        right_diagonal = [False] * (2*n-1)  # index 때문에 
        row = [False] * (2*n-1)            
        def recur_q(steps,sol) :
            if steps == n :
                ans.append(sol)
                return
            for i in range(0,n) :
                if row[i] or left_diagonal[i-steps+(n-1)] or right_diagonal[i+steps] :
                    continue
                else :
                    # board[i][steps] = 1 
                    row[i] = True
                    left_diagonal[i-steps+(n-1)] = True
                    right_diagonal[i+steps] = True
                    recur_q(steps+1,sol+[i+1])
                    row[i] = False
                    left_diagonal[i-steps+n-1] = False
                    right_diagonal[i+steps] = False
                    # board[i][steps] = 0 
        recur_q(0,[])
        return ans
    
start = time.time()
ob =Solution()

ans = ob.nQueen(10)
end= time.time()

print(len(ans))
print('hi')
print("time : {}".format(end-start))