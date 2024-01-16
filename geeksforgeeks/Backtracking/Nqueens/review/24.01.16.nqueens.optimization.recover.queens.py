#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        board = [[False for _ in range(n)] for _ in range(n)]
        sol = []
        def indxchk(x) :
            return x>=0 and x<n 
        def recur_q(steps,ans) :
            if steps == n:
                sol.append(ans)
                
            for i in range(n) :
                for k in range(1,steps+1) :
                    uprow = i-k
                    col = steps-k
                    downrow =i+k
                    if indxchk(uprow) and board[uprow][col]  : break
                
                    if indxchk(downrow) and board[downrow][col]  : break
                
                    if board[i][col] : break
                else :
                    board[i][steps] = True
                    recur_q(steps+1,ans+[i+1])
                    board[i][steps] = False
        
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