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
                for col, row in enumerate(ans) :
                    row-=1
                    if i+ steps == row+col or i == row or i-steps == row-col : break
               
                else:
                    recur_q(steps+1,ans+[i+1])
                    
                continue
                    
        recur_q(0,[])
        return sol
               
               
ob = Solution()

print(ob.nQueen(4))