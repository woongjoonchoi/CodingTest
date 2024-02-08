# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며 o
# , 놓여져 있는 곳의 좌표는 (x, y) 이다. 
# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.  o

#이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사  O
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다 O 

# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램

# 약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다  O
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다. O 

N,M,x,y, k = list(map(int,input().split()))

board= []
for i in range(N) :
    board.append(list(map(int,input().split())))
    
com_list = input().split()
dice = [0,0,0,0,0,0,0]

# temp_dice=[0,1,2,3,4,5,6]
# dice = temp_dice
# 1: 윗면 , 2 : 뒤 ,  3:동쪽,  4  : 서쪽  5 : 앞 ,6 :바닥

command = {'1' :[3,1,4,6] ,'2' : [4,1,3,6] ,'3' : [2,1,5,6] ,'4':[1,2,6,5]} 
cord_mov = {'1' :(0,1) , '2':(0,-1)  ,'3' :(-1,0) ,'4' :(1,0)}
def move(com,x,y) :
    temp = dice[com[0]]
    for  c in range(3) :
        dice[com[c]] = dice[com[c+1]]
    dice[com[3]] = temp
    
    if board[x][y] == 0 :
        board[x][y] = dice[6]
    else :
        dice[6] = board[x][y]
        board[x][y]= 0

def indsafe(x,y) :
    return x>=0 and x< N and y>=0 and y<M
for c in com_list :
    new_x ,  new_y= x + cord_mov[c][0] , y+cord_mov[c][1]
    if not indsafe(new_x, new_y) :  continue
    x ,y= new_x ,new_y 
    
    move(command[c] , x,y)
    print(dice[1])
        
# move(command['4'],2,2)
# print(dice)
# print(com_list)
        
    

