#User function Template for python3
import time
class Solution:
    def nQueen(self, n):
        # code here
        board =[ [0 for _ in range(n)] for _ in range(n)]
        
        ans = []
        def indxchk( x, y):
            
            return (x>=0 and x < n and y>=0 and y<n) 
        
        def recur_q(steps ,sol) :
            
            if steps == n:
                ans.append(sol)
                return
            for i in range(n) :
                
                diff =[]
                if board[i][steps] : continue
                
                for k in range(1,n-steps) :
                    up_row = i-k
                    down_row= i+k
                    col = steps+k
                    
                    if indxchk(i,col) and board[i][col] == 0 :
                        board[i][col] = 1
                        diff.append((i,col))
                    if indxchk(up_row,col) and board[up_row][col] == 0:
                        board[up_row][col] = 1
                        diff.append((up_row,col))
                    if indxchk(down_row,col) and board[down_row][col]== 0 :
                        board[down_row][col] = 1
                        diff.append((down_row,col))
                        
                recur_q(steps+1,sol+[i+1])
                
                for x,y in diff:
                    board[x][y] = 0
                
        recur_q(0,[])
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
ob = Solution()
start = time.time()
ans = ob.nQueen(10)
end = time.time()

print(f'time : {end-start}')

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
        
#         ob = Solution()
#         ans = ob.nQueen(n)
#         if(len(ans) == 0):
#             print("-1")
#         else:
#             for i in range(len(ans)):
#                 print("[",end="")
#                 for j in range(len(ans[i])):
#                     print(ans[i][j],end = " ")
#                 print("]",end = " ")
#             print()
                
# # } Driver Code Ends