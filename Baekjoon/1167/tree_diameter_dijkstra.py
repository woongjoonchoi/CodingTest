import sys
import heapq
def dijkstra(s ) :
    dist = [float('inf') for _ in range(V+1)]
    parent = [None for _ in range(V+1)]
    hq = []
    dist[s] = 0 
    # for i in range(1,V+1) :
    #     hq.append([dist[i] , i])
    # hq.append()
    hq.append([dist[s] , s])
    heapq.heapify(hq)
    
    for i in range(V) :
        # print(hq)
        est , u = heapq.heappop(hq)
        # print(f'est {est}  u {u}')
        if est == dist[u] : 
            # print('pass')
            for v,w in E[u] :
                if dist[v] > dist[u] + w :
                    dist[v] = dist[u]  + w
                    parent[v] = u
                    heapq.heappush(hq, [dist[v] , v])
    # print(dist)
    ans = max(dist[1:])
    # print(dist)
    return dist.index(ans)  , ans
V = int(input())
# E =[ [float('inf') for _ in range(V+1)] for _ in range(V+1) ]
E =  {} 


for k in range(V) :
    u , *c  = list(map(int,sys.stdin.readline().split()))
    E[u] = []
    for i in range(0,len(c)-1,2) :
        E[u].append( (c[i] ,c[i+1]) )
# for i in range(1,V+1) :
#     raw_edges  = list(map(int ,input().split()))
#     count = 0
#     vertex = raw_edges[count]
#     E[vertex] = []
#     count += 1

#     # vertex =
#     temp = []
#     while raw_edges[count] != -1 :
#         temp.append(raw_edges[count])
#         # temp.append()
#         if count %2 == 0:
#             # E[i][vertex] = raw_edges[count]
#             E[vertex].append(temp)
#             temp=[]
#         count +=1


# print(E)
new_source  , distance= dijkstra(1)
# print(new_source)
# print(distance)
_,ans = dijkstra(new_source)
print(ans)

# hq  =[[4,3],[1,3],[3,4],[5,6]]
# heapq.heapify(hq)
# while hq :
#     print(heapq.heappop(hq))

        