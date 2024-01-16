#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        board = [[False for _ in range(n)] for _ in range(n)]  ## 금지영역, False: 둘수잇음 ,True : 못둠
        
        sol = []
        
        def indxchk(x) : 
            return x>=0 and x < n
        def recur_q(steps,ans) :
            if steps == n :
                sol.append(ans)
                return
            for i in range(n) :
                if board[i][steps] : continue
            
                ban = [(i,steps)]
                board[i][steps] = True
                for k in range(1,n-steps) :
                    uprow = i-k
                    downrow = i+k
                    col = steps+k
                    
                    if indxchk(uprow) and not board[uprow][col] :
                        board[uprow][col] = True
                        ban.append((uprow,col))
                        
                    if indxchk(downrow) and not board[downrow][col] :
                        board[downrow][col] = True
                        ban.append((downrow,col))
                        
                    if not board[i][col] :
                        board[i][col] =True
                        ban.append((i,col))
                        
                recur_q(steps+1,ans+[i+1])
                
                for x, y in ban :
                    board[x][y] =False
                    
        recur_q(0,[])
        
        return sol

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends