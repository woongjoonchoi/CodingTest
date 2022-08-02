from collections import deque

# 1  .  set으로 순서 고려하지 않고 단어가 1개 다르면 변환할려함

# 2 . begin이 words안에 없다고 설명한적 없는데, 없다고 가정하고 함

def solution(begin, target, words):
    answer = 0
    
    graph = {}
    dist = {}

    for i , w in enumerate(words) :
        
        dist[w] = float('inf')
        graph[w] = []
        
        for j , ww in enumerate(words) :
            if i == j :
                continue
            count = 0
            for x,y in zip(ww,w) :
                if x!=y : 
                    count+=1
            if count==1:
                graph[w].append(ww)
    
    if begin not in graph.keys() :
        graph[begin] = []
        for i, w in enumerate(words) :
            count = 0
            for x,y in zip(begin,w) :
                if x!=y : 
                    count+=1
            if count == 1  :
                graph[w].append(begin)
                graph[begin].append(w)
      
        
    dist[begin] = 0
    queue = deque()
    visited = set()

    if target not in dist.keys() :
        return 0

    queue.append(begin)
    visited.add(begin)
    while queue :
        v = queue.popleft()
        for u in graph[v] : 
            if u not in visited :
                visited.add(u)
                queue.append(u)
                dist[u] = dist[v] + 1
    if dist[target] == float('inf') :
        answer = 0
    else :
        answer = dist[target]
    
    return answer