import heapq as hq

def solution(n, start, end, roads, traps):
    answer = float('inf')
    
    
    
    adj = [{} for _ in range(2**len(traps))] # key : src, val :  dst, weight]

    trap_bit = 0
    
#     traps의 i-th 를 방문하면 오른쪽에서 i-th bit만큼을 on
#     재 방문시 off
    
    dist = [[float('inf') for _  in range(n+1)] for _ in range(2**len(traps))]
#     distance estimate from s 
    
    for i in range(2**len(traps)) :
        roads_copy = roads[:]
        
        bin_traps = bin(i)[2:]
        
        for j , bits  in enumerate(bin_traps) :
            if bits == "1" :
                t = 
                for src, dst, w in roads_copy :
                    if not()
    
    for u , v, w  in roads :
        if u not in adj.keys() :
            adj[u] = []
            
        adj[u].append((v,w))
        
    for i in range(1,n+1) :
        if i not in adj.keys() :
            adj[i] = []
    
    queue = []
    
    for i in range(2 ** len(traps)) :
        for j in range(1,n+1) :
            queue.append((dist[i][j] , 10000 * i + j ))
    # hq.heappush(queue,(start,0))
    hq.heappush(queue,(0,start))
    
    hq.heapify(queue)
    dist[trap_bit][start]  = 0

    # past_node = -1
    while queue :
        # u, est = hq.heappop(queue)
        est , u = hq.heappop(queue)
        u= u%10000
        for i , t in enumerate(traps) : 
            if u == t:
                trap_bit = trap_bit ^ (1 << i)

                for j , (src, dst , w)  in enumerate(roads) : 

                    if not(src == u or dst == u)  :
                        continue
                    
          
                    adj[src].remove((dst,w))

                    adj[dst].append((src,w))
           
                    roads[j] = (dst,src,w)
            
        
        for v , w in adj[u] :
            temp_bit = 0
            for i , t in enumerate(traps) : 
                if v == t :
                    temp_bit = 1 << i
            if dist[trap_bit^temp_bit][v] > dist[trap_bit][u] + w :
                dist[trap_bit ^ temp_bit][v] = dist[trap_bit][u] + w 
                hq.heappush(queue,(dist[trap_bit^temp_bit][v] , 10000 * (trap_bit ^temp_bit) + v))
                
        # past_node = u
                
                
        

    
    for i in range(2**len(traps)) :
        answer = min(dist[i][end],answer)
    # print(answer)
    if answer == float('inf') :
        answer = 1
    return answer
# solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])

solution(	4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])