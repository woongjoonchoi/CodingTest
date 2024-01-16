#User function Template for python3

#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        board= [[False for _ in range(n)] for _ in range(n)]
        
        
        sol = []
        
        def issafe(i,steps) :
            
            def chksafe(row,col,rd,rc) :
                while col>=0 and row>=0 and row <n:
                    if board[row][col] : return False
                    row+=rd
                    col+=rc
                return True
            
            return chksafe(i,steps-1,0,-1) & \
                chksafe(i-1,steps-1,-1,-1) & \
                chksafe(i+1,steps-1,1,-1)
            

        def recur_q(steps,ans) :
        
            if steps == n :
                sol.append(ans)
                return 
            
            for i in range(n) :
                if issafe(i,steps) : 
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