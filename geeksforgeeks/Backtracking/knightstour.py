def check(x,y,n ) :
    if x >=0 and x<n and y>=0 and y<n :
        return True
    return False
def knightstour(board,val,x,y) :
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    
    if val == len(board) * len(board) :
        for b in board :
            print(b)
        exit(0)
    for i in range(8) :
        if check(x+dx[i],y+dy[i],len(board)) and board[x+dx[i]][y+dy[i]] == -1 :
            board[x+dx[i]][y+dy[i]] = val
            knightstour(board,val+1,x+dx[i],y+dy[i]) 
            board[x+dx[i]][y+dy[i]]  = -1 
    
def make_board(n) :
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[0][0] = 0 
    knightstour(board,1,0,0)
    # return


if __name__=='__main__' :
    make_board(8)