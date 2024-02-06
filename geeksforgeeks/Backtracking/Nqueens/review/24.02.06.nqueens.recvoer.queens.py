class Solution:
    def nQueen(self, n):
        # code here
        board= [[False for _ in range(n)] for _ in range(n)]
        
        sol =[]
        
        def chk_func(row,col,row_dir,col_dir) :
            while row>=0 and col>=0 and row<n and col< n:
                if board[row][col] :
                    return True
                col+=col_dir
                row+=row_dir
            return False
                
        def queen_chk(i,k):
            row = i
            col = k-1
            
            if chk_func(i,k-1,0,-1) : return True
            
            if chk_func(i-1,k-1,-1,-1) : return True
            
            if chk_func(i+1,k-1,1,-1) : return True
            
            # print(f"i:{i}  k : {k}return false")
            return False

                    
            
        def recur_q(steps,ans):
            # nonlocal sol
            if steps== n :
              sol.append(ans  )
              return
            
            for i in range(n) :
                if queen_chk(i,steps) : continue
                
                else : 
                    board[i][steps] = True
                    recur_q(steps+1,ans+[i+1])
                    board[i][steps] = False
            
        recur_q(0,[])
        return sol
        
        
 
# ob= Solution()

# print(ob.nQueen(3))

# print(len(ob.nQueen(4)))

# print(len(ob.nQueen(10)))


 
 