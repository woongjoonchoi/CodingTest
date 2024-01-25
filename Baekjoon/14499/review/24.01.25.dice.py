N,M, x,y ,K = list(map(int,input().split()))

board = []

for _ in range(N) :
    board.append(list(map(int,input().split())))
    
command = input().split()
dice =[0,0,0,0,0,0]

order = {'1' : [5,1,4,3] ,'2': [5,3,4,1] ,'3' : [3,0,1,2] ,'4' :[0,3,2,1]}
delta = {'1' : [0,1] ,'2' :[0,-1] ,'3' :[-1,0] ,'4' :[1 , 0 ]}

def move(x,y , order) :
    temp  = dice[order[0]]
    
    for i in range(len(order)-1) :
        dice[order[i]] = dice[order[i+1]]
    dice[order[3]]     = temp
    if board[x][y] == 0 :
        board[x][y] = dice[3]
    else : 
        dice[3] = board[x][y]
        board[x][y] = 0

def safe(x,y) :
    
    return x>=0 and x< N and y>=0 and y<M
for k in command : 
    x_mv= x+ delta[k][0]
    y_mv = y + delta[k][1]
    
    if not safe(x_mv,y_mv) : continue
    
    
    x ,y=x_mv , y_mv
    
    move(x,y,order[k])
    print(dice[1])
    
    
    