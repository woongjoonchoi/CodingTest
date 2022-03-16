from collections import deque

class Solution:
    def isBipartite(self, V, adj):
        
        color = [-1 for _ in range(V)]
        color[0] = 0
        flag = True
        
        s = set()
       # s.add(0)
      
        for i in range(V) :
            if i in s :
                continue
            queue = deque([])
            queue.appendleft(i)
            color[i] = 0
            while queue:
                node = queue.pop()
                for dest in  adj[node] :
                    if color[dest] - color[node] == 0 :
                        flag = False
                        break
                    if dest not in  s :
                        queue.appendleft(dest)
                        
                        s.add(dest)
                        
                        color[dest] = -color[node] +1
                if not flag :
                    break
            if not flag :
                break
            if len(s) == V :
                break
               
                    
        return flag
       
           
           
           
                
        #code here

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isBipartite(V, adj)
        if(ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends