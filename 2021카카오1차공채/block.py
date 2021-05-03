
# 0: E  , 1 : N
visited=[[ [float('inf'),float('inf')] for _ in range(100)] for _ in range(100)]

# def isValid(board,x ,y) :
#     if 

# 상 하 좌 우 
delta = [(-1,0) ,(1,0),(0,-1),(0,1)  ]

# N
# rotate_1 = [(-1,0), (1,0)]

rotate_0 = [(-1,0,1) , (0,0,1) , (-1,1,1) , (0,1,1) ]
valid_0=[(-1,1) , (1,1) , (-1,0) , (1,0)]
# E
# rotate_0 = [(0,1) , (0,-1)]

rotate_1 = [(0,-1,0) ,(0,0,0) ,(1,0,0) , (1,-1,0)]
valid_1=[(1,-1) , (1,1) , (0,1) , (0,-1)]
# E , N

dr =[(0,1),(1,0)]

def rtValid(board ,r ,i,u):
    if r[2] == 1 :
        if board[u[0]+valid_0[i][0]][u[1]+valid_0[i][1]] == 1:
            return False
    elif r[2] == 0:
        if board[u[0]+valid_1[i][0]][u[1]+valid_1[i][1]] == 1:
            return False
    return True
def isValid(v, n,board) :

    if not (v[0] >= 0 and v[1] >=0  and v[0] < n and v[1] < n) :
        return False
    if not(v[0] + dr[v[2]][0] <n and v[1] + dr[v[2]][1] <n and  v[0] + dr[v[2]][0] >=0 and v[1] + dr[v[2]][1] >=0 ): 
        return False
    if board[v[0]][v[1]] == 1 or board[  v[0] + dr[ v[2] ][0] ][ v[1] + dr[ v[2]][1] ] == 1 :
        return False

    return True
def arrive(n) : 
    if visited[n-1][n-2][0] !=float('inf') or visited[n-2][n-1][1] !=float('inf') :
        return True
    return False
def rotate(info) :
    x, y, d = info
    li = []
    if d== 0:
        for r in rotate_0 :
            li.append((x+r[0] ,y+r[1] , r[2]))
    else :
        for r in rotate_1 :
            li.append((x+r[0] ,y+r[1] , r[2]))
    return li
def bfs(board):

    global visited
    q= []
    n = len(board)
    # (x,y,d) 0: E , 1: S
    q.append((0,0,0))
    visited[0][0][0] = 0
    while q  and not arrive(n):
        u = q.pop(0)
        for d in delta:
            v = (d[0]+u[0],d[1]+u[1],u[2])
            if isValid(v,n,board) and visited[v[0]][v[1]][u[2]] > visited[u[0]][u[1]][u[2]] + 1 : 
                visited[v[0]][v[1]][u[2]] = visited[u[0]][u[1]][u[2]] + 1 
                q.append(v)
        rt = rotate(u)
        for i,r in enumerate(rt) :
            if  isValid(r,n,board) and visited[r[0]][r[1]][r[2]] > visited[u[0]][u[1]][u[2]] + 1  and  rtValid(board,r,i,u) :
                visited[r[0]][r[1]][r[2]] = visited[u[0]][u[1]][u[2]] + 1 
                q.append(r)
        # roate : r,c  ,  r,c+1

def solution(board):
    answer = 0
    bfs(board)
    n=len(board)
    for i in range(n):
        print(visited[i][:n])
    answer = min(visited[n-1][n-2][0] , visited[n-2][n-1][1])
    print(answer)
    return answer


# print(rotate((0,0,0)))
solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])