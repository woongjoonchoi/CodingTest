import heapq as hq

def solution(n, start, end, roads, traps):
    answer = float('inf')
    
    
    
    adj = [{} for _ in range(2**len(traps))] #  i , : which_trap visit , key : src, val :  dst, weight 

    trap_bit = 0
    
#     traps의 i-th 를 방문하면 오른쪽에서 i-th bit만큼을 on
#     재 방문시 off
    
    # dist = [[float('inf') for _  in range(n+1)] for _ in range(2**len(traps))]
    
    dist = {}
#     distance estimate from s 
    
    
    def make_adj(i) :
    # for i in range(2**len(traps)) :
        roads_copy = roads[:]
        bin_str = bin(i)[2:]

        bin_traps = (len(traps)-len(bin_str)) * "0"+bin_str

        for k in range(1,n+1) :
            adj[i][k] = []
        for j , bits  in enumerate(bin_traps) :

            if bits == "1" :
                for ind , (src, dst, w )in enumerate(roads_copy) :
                    
                    if not(src == traps[len(traps) -1-j]  or dst == traps[len(traps)-1-j]) :
                        continue
                    roads_copy[ind] = (dst,src,w)
        for j ,(src, dst, w )in enumerate(roads_copy) :
            adj[i][src].append((dst,w))
            

    queue = []
    
    # for i in range(2 ** len(traps)) :
    #     for j in range(1,n+1) :
    #         queue.append((dist[i][j] , 10000 * i + j ))
    # hq.heappush(queue,(start,0))
    
    
    hq.heappush(queue,(0,start))
    
    hq.heapify(queue)
    
    dist[0] = [float('inf') for _  in range(n+1)]
    dist[trap_bit][start]  = 0

    # past_node = -1
    while queue :
        # u, est = hq.heappop(queue)
        est , u = hq.heappop(queue)
        trap_bit = u //10000
        u= u%10000

        if not adj[trap_bit].keys() :
            make_adj(trap_bit)
            
        if trap_bit not in dist.keys() :
            dist[trap_bit] = [float('inf') for _  in range(n+1)]
        for v , w in adj[trap_bit][u] :
            temp_bit = 0
            for i , t in enumerate(traps) : 
                if v == t :
                    temp_bit = 1 << (i)
            if trap_bit^temp_bit not in dist.keys() :
                dist[trap_bit^temp_bit] = [float('inf') for _  in range(n+1)]
            if dist[trap_bit^temp_bit][v] > dist[trap_bit][u] + w :
                dist[trap_bit ^ temp_bit][v] = dist[trap_bit][u] + w 
                hq.heappush(queue,(dist[trap_bit^temp_bit][v] , 10000 * (trap_bit ^temp_bit) + v))
                
    
        if u == end :
            break
                
        # past_node = u
                
                
        

    
    for i in range(2**len(traps)) :
        if i not in dist.keys() :
            continue
        answer = min(dist[i][end],answer)
    # print(answer)
    if answer == float('inf') :
        answer = 1
    return answer
# solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])

solution(	4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])