
import time

class Solution:
    def nQueen(self, n):
        # code here
        ans = []
        def indxchk(x,y):
            return x>=0 and x< n and y>=0 and y<n
        board =[ [0 for _ in range(n)] for _ in range(n)]
        def recur_q(steps,sol):
            if steps == n :
                ans.append(sol)
                return
            for i in range(n) :
                
                for k in range(1,steps+1) :
                    up_row = i-k
                    down_row = i+k
                    col = steps-k
                    if (indxchk(up_row,col) and board[up_row][col] == 1) :
                        break
                    if ( indxchk(down_row,col) and board[down_row][col] == 1 )  :
                        break
                    if ( indxchk(i,col) and board[i][col] == 1) :
                        break
                else :
                    board[i][steps] = 1
                    recur_q(steps+1,sol+[i+1])
                    board[i][steps] = 0
                    
                
            
        recur_q(0,[])
        
        return ans

start = time.time()

ob = Solution()
kk = ob.nQueen(10)

end = time.time()
print(len(kk))
print(f'Time : {end-start}')