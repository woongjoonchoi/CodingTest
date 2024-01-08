class Solution:
    def nQueen(self, n):
        # code here
        ans = []

        # board =[ [0 for _ in range(n)] for _ in range(n)] #save for Queen
        
        
        # left_diagonal = [False]* (2n+1)
        # right_diagonal = [False]* (2n+1)
        # left_row = [False] * n
        def recur_q(steps,sol):
            if steps == n :
                ans.append(sol)
                return
            for i in range(n) :
                for y,x in enumerate(sol) :
                    row = x-1
                    if row == i or y + row == i + steps or row-y == i-steps :
                        break
                
                else :
                    recur_q(steps+1,sol+[i+1])
            
        recur_q(0,[])
        
        return ans