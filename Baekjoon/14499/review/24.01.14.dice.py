N,M,x,y,K = map(int , input().split()) 

board = []
command = None
dice = [0,0,0,0,0,0]
for _ in range(N) :
    board.append(list(map(int , input().split())))
command = list(map(int , input().split()))

def indx_safe(x,y) :
    return x>=0 and x<N and y>=0 and y< M
# x,y 움직이고 나서의  주사위 좌표 , b : 바닥인 주사위면 
def board_chk(x,y) :
    if board[x][y] == 0 : board[x][y] = dice[3]
    else : 
        dice[3] = board[x][y] 
        board[x][y] = 0
    print(dice[1])
# x,y 는 움직이기 전 주사위 좌표 

def north(x,y) :
    if not indx_safe(x-1,y) : return x, y 
    temp = dice[0]
    for i in range(3):
        dice[i] = dice[i+1]
    dice[3] = temp
    board_chk(x-1,y)
    return x-1,y
    
def south(x,y) :
    if not indx_safe(x+1,y) : return x, y 
    temp = dice[3]
    for i in range(2,-1,-1) :
        dice[i+1] = dice[i]
        
    dice[0] = temp
    board_chk(x+1,y)
    return x+1 ,y
    
def west(x,y) :
    if not indx_safe(x,y-1) : return x, y 
    temp = dice[1]
    seq = [1,5,3,4]
    for i in range(len(seq)-1) :
        dice[seq[i]] = dice[seq[i+1]]
    dice[4] =temp
    board_chk(x,y-1)
    return x,y-1
def east(x,y) :
    if not indx_safe(x,y+1) : return x, y 
    temp = dice[5]
    seq = [5,1,4,3]
    for i in range(len(seq)-1) :
        dice[seq[i]] = dice[seq[i+1]]
    dice[3] =temp
    board_chk(x,y+1)
    return x,y+1
        
snip = {1 :east , 2: west,3:north,4:south}

for k in command : 
    x,y  = snip[k](x,y)


# print('south check')
# for i in range(2,-1,-1) :
    
#     print(f'{i} -> {i+1}')
    
# print('north check')
# for i in range(3):
#     print(f'{i} <- {i+1}')


# print('west check')

# seq = [1,5,3,4]
# for i in range(len(seq)-1) :
#     print(f'{seq[i]} <- {seq[i+1]}')
    
# print('east check')

# seq = [5,1,4,3]
# for i in range(len(seq)-1) :
#     print(f'{seq[i]} <- {seq[i+1]}')