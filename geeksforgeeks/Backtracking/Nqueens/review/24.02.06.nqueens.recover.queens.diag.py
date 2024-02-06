class Solution:
    def nQueen(self, n):
        # code here
        # board =[ [False for _ in range(n)] for _ in range(n)]
        up_diag =[False for _ in range(2*n-1)]
        low_diag = [False for _ in range(2*n-1)]
        same_row = [False for _ in range(n)]
        
        
        sol = []
        def recur_q(steps,ans) :
            
            if steps == n :
                sol.append(ans)
                return
            
            for i in range(n) :
                if up_diag[steps+i] or same_row[i] or low_diag[i-steps+n-1] : continue
                
                up_diag[steps+i]  = True
                same_row[i] = True
                low_diag[i-steps+n-1] = True
                
                recur_q(steps+1,ans+[i+1])
                up_diag[steps+i]  = False
                same_row[i] = False
                low_diag[i-steps+n-1] = False
                
        recur_q(0,[])            

        return sol
    
ob =Solution()

print(ob.nQueen(4))
    
    