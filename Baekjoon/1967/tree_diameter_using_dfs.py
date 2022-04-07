import sys

n = int(input())

adj = [[] for _ in range(n+1)]

for i in range(n-1) :
    parent , child ,weight = map(int ,sys.stdin.readline().split())
    adj[parent].append((child,weight))
    adj[child].append((parent,weight))
    
max_diameter = 0

def dfs(root) :
    
    global max_diameter
    
    visited = set()
    stack = []
    
    visited.add(root)
    stack.append(root)
    
    while stack :
        
        node = stack.pop()
        visited.add(node)
        
        
    
    