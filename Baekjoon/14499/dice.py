import sys


n,m,x,y,k = list(map(int, sys.stdin.readline().strip().split()))

matrix = [list(map(int, sys.stdin.readline().split()))  for _ in range(n) ]



command = list(map(int, sys.stdin.readline().split()))

#1 : 동쪽

#2 : 서쪽

#3 : 북쪽

#4 : 남쪽

#input : n 세로크기 , m 가로크기 , x 주사위 좌표(0<=x<N) , y 주사위 좌표 (0<=y<M) , k 명령의 개수
# output : 주사위 윗면에 쓰여있는 수, 

#constraint : 맵 바깥 이동시 그 명령 무시 
#  이동한 칸 == 0 : 주사위 바닥면 -> 칸
#  이동한 칸 != 0 : 칸 -> 주사위  ,칸 = 0

vert_dice = [0,0,0]
hori_dice = [0,0,0]
bottom = 0 

def check(x,y,n,m) :
    if 0<=x<n and 0<=y<m : 
        return True
    return False

dx =[0,0,0,-1,1]
dy = [0,1,-1,0,0]
for i in command : 
    if not check(x+dx[i],y+dy[i],n,m) :
        continue
    if i== 1 :
        temp  =  hori_dice[-1]
        for h in range(len(hori_dice)-1,0,-1) :
            hori_dice[h] = hori_dice[h-1]
        hori_dice[0] = bottom
        bottom = temp
        vert_dice[1] = hori_dice[1]
        y+=1
    elif i == 2 :
        temp = hori_dice[0]
        for h in range(1,len(hori_dice)) :
            hori_dice[h-1] = hori_dice[h]
        hori_dice[-1] = bottom
        bottom = temp
        vert_dice[1] = hori_dice[1]
        y-=1
    elif i == 3 :
        temp = vert_dice[-1]
        for v in range(len(vert_dice)-1 , 0, -1) :
            vert_dice[v] = vert_dice[v-1]
        vert_dice[0] = bottom
        bottom = temp
        hori_dice[1] = vert_dice[1]
        x-=1
    elif i == 4:
        temp = vert_dice[0]
        for v in range(1,len(vert_dice)) :
            vert_dice[v-1] = vert_dice[v]
        vert_dice[-1] =bottom
        bottom= temp
        hori_dice[1] = vert_dice[1]
        x+=1
    if matrix[x][y] !=0 :
        bottom = matrix[x][y]
        matrix[x][y] = 0
    else :
        matrix[x][y] = bottom
    print(vert_dice[1])


# print(matrix)

# hori_dice = [1,2,3]
# bottom = 0
# temp  =  hori_dice[-1]
# for h in range(len(hori_dice)-1,0,-1) :
#     hori_dice[h] = hori_dice[h-1]
# hori_dice[0] = bottom
# bottom = temp

# hori_dice = [1,2,3]
# bottom = 0
# temp = hori_dice[0]
# for h in range(1,len(hori_dice)) :
#     hori_dice[h-1] = hori_dice[h]
# hori_dice[-1] = bottom
# bottom = temp
# # vert_dice[1] = hori_dice[1]

# print(hori_dice)
# print(bottom)