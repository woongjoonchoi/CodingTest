#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        ans = []

        # board =[ [0 for _ in range(n)] for _ in range(n)] #save for Queen
        
        
        left_diagonal = [False]* (2*n+1)
        right_diagonal = [False]* (2*n+1)
        left_row = [False] * n
        def recur_q(steps,sol):
            if steps == n :
                ans.append(sol)
                return
            for i in range(n) :
                if left_row[i] or left_diagonal[i-steps+n] or right_diagonal[i+steps] :
                    continue
                else :
                    left_row[i] = True
                    left_diagonal[i-steps+n] = True
                    right_diagonal[i+steps] = True
                    recur_q(steps+1,sol+[i+1])
                    left_row[i] = False
                    left_diagonal[i-steps+n] = False
                    right_diagonal[i+steps] = False
                
            
            
        recur_q(0,[])
        
        return ans

        # code here


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