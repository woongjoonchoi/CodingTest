import sys
from collections import deque
n = int(input())

adj = [[] for _ in range(n+1)]

for i in range(n-1) :
    parent , child , weight = list(map(int,sys.stdin.readline().split()))
    adj[parent].append((child ,weight))
    adj[child].append((parent,weight))
    
    
max_diameter = 0


# def diameter(root) :  
    
#     global max_diameter
#     if len(adj[root]) == 0:
#         return 0
    
#     max1 , max2 = 0 , 0
    
#     for child , weight in adj[root] :
#         height = diameter(child)
#         weight += height
#         if weight >= max1 :
#             max2 = max1
#             max1 = weight
#         elif weight > max2 : 
#             max2 = weight
    
#     max_diameter = max(max1 + max2 , max_diameter)        
    
#     return max1

max_height = 0



def bfs(root) :
    global max_diameter
    queue = deque([])

    visited = [False for _ in range(n+1)]
    diameter = [0 for _ in range(n+1)]
    queue.append(root)
    while queue :
        
        root = queue.popleft()
        visited[root]  = True
            
        for child,weight in adj[root] :
            if not visited[child]  :
                queue.append(child)
                if diameter[root] + weight > diameter[child] :
                    diameter[child] = diameter[root] + weight
    ind = 1
    max_dist = diameter[0]     
    for i in range(1,n+1) :
        if diameter[i] > max_dist : 
            ind = i 
            max_dist = diameter[i]
            max_diameter = diameter[i]
            
    
    return ind 
    
u = bfs(1)
bfs(u)

# diameter(1)
print(max_diameter)
            
    