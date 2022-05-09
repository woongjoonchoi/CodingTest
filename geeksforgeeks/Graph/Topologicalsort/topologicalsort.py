class Solution:
    
    #Function to return list containing vertices in Topological order.
    
    def dfs(self,u,adj , visited,topo) :
        
        if u in visited :
            return
        visited.add(u)
        
        for v in adj[u] :
            self.dfs(v,adj,visited,topo)
        
        topo.append(u)
        
        
        
        
        
    
    def topoSort(self, V, adj):
        # Code here
        
        # stack = []
        
        visited = set()
        
        topo = []
        # stack.append(0)
        
        # while stack :
            
        #     u =  stack.pop(0)
        
        for v in range(V) :
            self.dfs(v,adj,visited , topo)
        
        topo.reverse()
        # print("topo")
        # print( topo)
        
        return topo
            
    

#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends