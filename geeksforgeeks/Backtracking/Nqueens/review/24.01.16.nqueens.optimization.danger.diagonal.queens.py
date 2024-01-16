#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        left_diag =[False] * (2*n-1)  # -3 ~ 3
        right_diag = [False] * (2*n-1)  #0 ~ 6
        same_row = [False] * n
        
        sol =[]
        def recur_q(steps,ans) :
            
            if steps == n:
                sol.append(ans)  
                
                return 
            
            for i in range(n) :
                if same_row[i] or left_diag[i-steps+n-1] or right_diag[i+steps] : continue
            
                else : 
                    left_diag[i-steps+n-1] = True
                    right_diag[i+steps] = True
                    same_row[i] = True
                    recur_q(steps+1,ans+[i+1])
                    left_diag[i-steps+n-1] = False
                    right_diag[i+steps] = False
                    same_row[i] = False
                    
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