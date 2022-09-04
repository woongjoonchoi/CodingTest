import heapq as hq

def solution(n, start, end, roads, traps):
    answer = 0
    
    adj = {}
    trap_bit = 0
    
#     traps의 i-th 를 방문하면 오른쪽에서 i-th bit만큼을 on
#     재 방문시 off
    
    dist = [[float('inf') for _  in range(1001)] for _ in range(1024)]
#     distance estimate from s 
    
    for u , v, w  in roads :
        if u not in adj.keys() :
            adj[u] = []
            
        adj[u].append((v,w))
    
    queue = []
    
    hq.heappush(queue,(start,0))
    dist[trap_bit][start]  = 0

    past_node = -1
    while queue :
        u, est = hq.heappop(queue)
        u= u%10000
        for i , t in enumerate(traps) : 
            if u == t:
                trap_bit = trap_bit ^ (1 << i)
                for v , w in adj[past_node] :
                    adj[u].delete(v,w)
                    if v not in adj.keys() :
                        adj[v] = []
                    adj[v].append(u,w)
                
            
        
        for v , w in adj[u] :
            if dist[trap_bit][v] > dist[trap_bit][u] + w :
                dist[trap_bit][v] = dist[trap_bit][u] + w 
                hq.heappush(queue,(10000 * trap_bit + v,dist[trap_bit][v]))
                
        past_node = u
                
                
        

    
    for i in range(1024) :
        answer = min(dist[i][end])
    return answer

solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])