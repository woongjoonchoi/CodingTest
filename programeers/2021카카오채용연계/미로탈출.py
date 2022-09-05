import heapq as hq

def solution(n, start, end, roads, traps):
    answer = float('inf')
    
    adj = {}  # key : src, val :  dst, weight

    trap_bit = 0
    
#     traps의 i-th 를 방문하면 오른쪽에서 i-th bit만큼을 on
#     재 방문시 off
    
    dist = [[float('inf') for _  in range(1001)] for _ in range(1024)]
#     distance estimate from s 
    
    for u , v, w  in roads :
        if u not in adj.keys() :
            adj[u] = []
            
        adj[u].append((v,w))
        
    for i in range(1,n+1) :
        if i not in adj.keys() :
            adj[i] = []
    
    queue = []
    
    hq.heappush(queue,(start,0))
    dist[trap_bit][start]  = 0

    # past_node = -1
    while queue :
        u, est = hq.heappop(queue)
        u= u%10000
        for i , t in enumerate(traps) : 
            if u == t:
                trap_bit = trap_bit ^ (1 << i)

                for j , (src, dst , w)  in enumerate(roads) : 
                    # if src == u :
                    #     adj[src].remove((dst,w))
                    #     if dst not in adj.keys() :
                    #         adj[dst] = []
                    #     adj[dst].append((src,w))
                    # if dst == u :
                    if not(src == u or dst == u)  :
                        continue
                    adj[src].remove((dst,w))
                    # if dst not in adj.keys() :
                    #     adj[dst] = []
                    adj[dst].append((src,w))
                    
                    roads[j] = (dst,src,w)
            
        
        for v , w in adj[u] :
            temp_bit = 0
            for i , t in enumerate(traps) : 
                if v == t :
                    temp_bit = 1 << i
            if dist[trap_bit^temp_bit][v] > dist[trap_bit][u] + w :
                dist[trap_bit ^ temp_bit][v] = dist[trap_bit][u] + w 
                hq.heappush(queue,(10000 * (trap_bit ^temp_bit) + v,dist[trap_bit^temp_bit][v]))
                
        # past_node = u
                
                
        

    
    for i in range(1024) :
        answer = min(dist[i][end],answer)
    print(answer)
    return answer

# solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])

solution(	4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])