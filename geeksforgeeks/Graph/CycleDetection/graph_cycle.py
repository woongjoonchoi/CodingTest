#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    
    def dfs(self,u,adj,visited,topo) :
        
        if u in visited :
            return
        
        visited.add(u)
        
        for v in adj[u] :
            self.dfs(v,adj,visited,topo)
            
        topo.append(u)
        
        
    def isCyclic(self, V, adj):
        
        visited = set()
        
        topo = []
        
        for v in range(V) :
            self.dfs(v,adj,visited,topo)
            
        # topo = topo[::-1]
        
        # print(topo)
        
        table = [-1 for _ in range(V)]
        
        for i , t in enumerate(topo) :
            table[t] = V-1-i
        
            
        # print(table)
        
        flag = False
        
        for v in range(V) :
            for u in adj[v] :
                if table[u] < table[v] :
                    flag = True
                    break
                elif v == u :
                    flag= True
                    break
            if flag == True :
                break
        
 

        return flag
            
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends