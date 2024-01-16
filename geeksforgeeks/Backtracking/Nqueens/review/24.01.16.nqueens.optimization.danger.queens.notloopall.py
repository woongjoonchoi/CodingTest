#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        board= [[False for _ in range(n)] for _ in range(n)] # False Safe True Danger
        
        
        sol = []
        
        def addban(i,steps) :
            ban = [(i,steps)]
            board[i][steps] = True
            
            def chkban(row,col,dr,dc) :
                while col>=0 and col <n and row >=0 and row< n:
                    if not board[row][col] :
                        ban.append((row,col))
                        board[row][col] = True
                    row +=dr
                    col +=dc
            
            chkban(i,steps+1,0,1)
            chkban(i+1,steps+1,1,1)
            chkban(i-1,steps+1,-1,1)
                
                
            return ban

        def recur_q(steps,ans) :
        
            if steps == n :
                sol.append(ans)
                return 
            
            for i in range(n) :
                if board[i][steps]  : continue
                
                ban =  addban(i,steps) 
                recur_q(steps+1,ans+[i+1])
                
                for x, y in ban :
                    board[x][y] = False
                
                
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