from collections import deque



# node를 간격을 1로 표현하는 2d array로 사용하면 edge 관계가 아닌 node가 edge관계라 표현됨.
# 따라서 , 간격을 늘려서 , edge관계가 아니도록 표현
#1 . 노드를 grid의 모든  point, edge를 갈 수있는 외각선으로

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    
    coord = [[0 for _ in range(104)]  for  _ in range(104)]
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
        
    for x1 , y1, x2 , y2 in rectangle :
        for i in range(2*x1,2*x2+1) :
            for j in range(2*y1,2*y2+1) :
                coord[i][j] = 1
                
    for x1,y1,x2,y2 in rectangle :
        for i in range(2*x1+1,2*x2) :
            for j in range(2*y1+1,2*y2) :
                coord[i][j] = 0
              
    visited =[[float('inf') for _ in range(104)]  for  _ in range(104)]
    
    queue = deque([])
    
    queue.append((2*characterX,2*characterY))
    visited[2*characterX][2*characterY] = 0
    
    while queue :
        u , v = queue.popleft()
 
        for deltax,deltay in zip(dx,dy) :
            if (coord[u+deltax][v+deltay] ==1  
                and visited[u+deltax*2][v+deltay*2] == float('inf') ) :
                queue.append((u+deltax*2, v+deltay*2))
                visited[u+deltax*2][v+deltay*2] = visited[u][v] +1
                
        if visited[itemX*2][itemY*2] != float('inf') :
            answer = visited[itemX*2][itemY*2]
            break


    return answer