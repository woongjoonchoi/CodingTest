def check(x,y,n ) :
    if x >=0 and x<n and y>=0 and y<n :
        return True
    return False
def knightstour(board,val,x,y,dx,dy) :
    if val == len(board) * len(board) : 
        return True 

    for i in range(8) :
        if check(x+dx[i],y+dy[i],len(board)) and board[x+dx[i]][y+dy[i]] == -1 :
            board[x+dx[i]][y+dy[i]] = val
            if knightstour(board,val+1,x+dx[i],y+dy[i],dx,dy) :
                return True
            board[x+dx[i]][y+dy[i]]  = -1 

def make_board(n) :
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[0][0] = 0 
    if knightstour(board,1,0,0,dx,dy) :    
        for b in board :
            print(b)
    else :
        print("No solution")
    # return


if __name__=='__main__' :
    make_board(8)