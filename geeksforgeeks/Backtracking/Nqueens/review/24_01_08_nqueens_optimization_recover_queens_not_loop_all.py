#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        ans = []

        board =[ [0 for _ in range(n)] for _ in range(n)]
        
        def issafe(i,steps) :

            col = steps
            while col>=0 : 
                if board[i][col] == 1 :
                    return False
                col -=1
            col = steps
            up_row = i
            while col>=0 and up_row>=0 :
                if board[up_row][col] ==1 :
                    return False
                col -=1
                up_row -=1
            col = steps
            down_row = i
            while col>=0 and down_row < n : 
                if board[down_row][col] == 1 :
                    return False
                col -= 1
                down_row +=1
            return True
            # down_row = i+k
        def recur_q(steps,sol):
            if steps == n :
                ans.append(sol)
                return
            for i in range(n) :
                
                if not issafe(i,steps) :
                    continue
                else :
                    board[i][steps] = 1
                    recur_q(steps+1,sol+[i+1])
                    board[i][steps] = 0
                    
                
            
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