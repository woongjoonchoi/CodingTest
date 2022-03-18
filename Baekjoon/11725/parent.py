import sys

N = int(input())

adj = [[]for _ in range(N+1)]

for k in range(N-1) :
    u, v = map(int,sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [0 for _ in range(N+1)]
    
marked = set()

stack = []
# def dfs(u) :
    
#     marked.add(u)
#     for v in adj[u] :
#         if v not in marked :
#             parent[v] = u
#             dfs(v)

# dfs(1)

stack.append(1)
while stack : 
    u = stack.pop()
    marked.add(u)
    for v in adj[u] :
        if v not in marked :
            stack.append(v)
            parent[v] = u
            # break
    

print('\n'.join(map(str, parent[2:])))
        
    