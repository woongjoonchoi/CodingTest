#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        
        sol = []
        def recur_q(steps,ans) :
            
            if steps == n :
                
                sol.append(ans)
                return 
            
            for i in range(n) :
                
                for col,row  in enumerate(ans) :
                    row -=1
                    
                    if row == i or row-col == i-steps or row+col == i+steps :
                        break
                else :
                    recur_q(steps+1,ans+[i+1])
                
        
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