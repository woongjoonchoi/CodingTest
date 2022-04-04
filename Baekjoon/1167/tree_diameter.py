import sys
from collections import deque
v = int(input())

adj = [[] for _ in range(v+1)]



for k in range(v) :
    u , *c  = list(map(int,sys.stdin.readline().split()))
    for i in range(0,len(c)-1,2) :
        adj[u].append( (c[i] ,c[i+1]) )

max_diameter=  0
def bfs(root) :
    global v
    global max_diameter

    visited = set()
    
    diameter = [0 for _ in range(v+1)]
    
    queue = deque([])
    
    queue.append(root)
    
    while queue :
        
        node = queue.popleft()
        # visited[node] = True
        visited.add(node)
        
        
        for child,weight in adj[node] :
            # if not visited[child] :
            if child not in visited : 
                queue.append(child)
                # print(f'child : {child} node : {node}')
                if diameter[node] + weight > diameter[child] :
                    diameter[child] = diameter[node] + weight
    
    
    ind = 1
    max_dia = 0
    for i in range(1 , len(diameter)) : 
        if  diameter[i]>max_dia :
            ind = i 
            max_dia , max_diameter = diameter[i] , diameter[i]
        
    return ind

u = bfs(1)

bfs(u)

print(max_diameter)