import numpy as np




# 0: E  , 1 : N
visited=[[ [0,0] for _ in range(100)] for _ in range(100)]

# def isValid(board,x ,y) :
#     if 

# 상 하 좌 우 
delta = [(-1,0) ,(1,0),(0,-1),(0,1)  ]

# N
rotate_1 = [(-1,0), (1,0)]
# E
rotate_0 = [(0,1) , (0,-1)]

    
def rotate(info) :
    x, y, d = info
    li = []
    if d== 0:
        p = (x+rotate_0[0][0] , y+rotate_0[0][1]-1 ,1)
        li.append(p)
        p = (x+rotate_0[1][0] , y+rotate_0[1][1] ,1)
        li.append(p)
        p = (x+1+rotate_0[0][0] , y+rotate_0[0][1]-1 ,1)
        li.append(p)
        p = (x+1+rotate_0[1][0] , y+rotate_0[1][1] ,1)
        li.append(p)
    else :
        p = (x+rotate_1[0][0] , y + rotate_1[0][1] , 0 )
        li.append(p)
        p = (x+rotate_1[1][0]-1 , y + rotate_1[1][1] , 0 )
        li.append(p)
        p = (x+rotate_1[0][0] , y + 1+rotate_1[0][1] , 0 )
        li.append(p)
        p = (x+rotate_1[1][0] -1  , y + 1+rotate_1[1][1] , 0 )
        li.append(p)
    return li


def bfs(board):

    global visited
    q= []
    # (x,y,d) 0: E , 1: S
    q.append((0,0,0))
    while q :
        u = q.pop(0)

def solution(board):
    answer = 0
    return answer