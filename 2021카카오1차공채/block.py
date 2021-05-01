

# 0: E  , 1 : S
visited=[[ [0,0] for _ in range(100)] for _ in range(100)]

# def isValid(board,x ,y) :
#     if 

# 상 하 좌 우 
delta = [(-1,0) ,(1,0),(0,-1),(0,1)  ]

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