class Solution:
    def nQueen(self, n):
        
        board  =[[ False for _ in range(n)] for _ in range(n)]
        
        sol = []
        
        def indchk(row,col) :
            return row>=0 and row < n and col>=0 and col <n
        
        
        def recur_q(steps,ans) :
            
            if steps == n :
                
                sol.append(ans)
                return
            
            for i in range(n) :
                if board[i][steps] : continue
                
                row,col = i,steps
                # if steps == 2 : print(board)
                dangers_new=[[row,col]]
                board[row][col] = True
                row,col = i-1,steps+1
                while indchk(row,col) :
                    if not board[row][col] :
                        dangers_new.append([row,col])
                        board[row][col] = True
                    row-=1
                    col+=1
                row,col = i,steps+1
                while indchk(row,col) :
                    if not board[row][col] : 
                        dangers_new.append([row , col])
                        board[row][col] = True
                    
                    col+=1
                row,col = i+1,steps+1
                while indchk(row,col) :
                    if not board[row][col] : 
                        dangers_new.append([row , col])
                        board[row][col] = True
                    row+=1
                    col+=1
                recur_q(steps+1,ans+[i+1])
                
                for r,c in dangers_new:
                    board[r][c] = False
                    
            
            
            
        
        recur_q(0,[])
        return sol
        
ob = Solution()

print(ob.nQueen(4))