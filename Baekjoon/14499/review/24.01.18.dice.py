N,M,x,y,k = list(map(int,input().split()))

board = []

for _ in range(N) :
    board.append(list(map(int , input().split())))
    
command = input().split()

direc = {'1' :(0,1) , '2' :(0,-1) , '3':(-1,0) , '4' :(1,0)}
dice = [0,0,0,0,0,0]

dice_move={'3':[3,0,1,2]  ,'4' : [0,3,2,1] , '2' : [3,4,1,5] , '1' : [3,5,1,4]}

def indxsafe(x,y) :
    return x >=0 and x < N and y>=0 and y < M 

def move(seq,x,y,dice) :
    temp = dice[seq[0]]
    
    for i in range(len(seq)-1):
        dice[seq[i]] = dice[seq[i+1]]
    dice[seq[-1]] = temp 
    if board[x][y] == 0 :
        board[x][y] = dice[3]
    else : 
        dice[3] = board[x][y] 
        board[x][y] = 0
for k in command :
    temp_x = x + direc[k][0]
    temp_y = y + direc[k][1]
    if not indxsafe(temp_x,temp_y) : continue
    
    x = temp_x
    y=temp_y
    move(dice_move[k],x,y,dice)
    print(dice[1])
    