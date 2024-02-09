#  노드에 늑대와 양이 한 마리씩 놓여 있습니다
# 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모으려 합니다
# 노드를 방문할 때 마다 해당 노드에 있던 양과 늑대가 당신을 따라오게 됩니다
#  당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다
# 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려 합니다.
# 루트 노드에는 항상 양이 있습니다
# 0은 양, 1은 늑대를 의미합니다.
import time
def adj(u,g,info):
    adj_list = []
    for v in g[u[1]] :
        take_node = list(u[0])
        me , sheep ,wolf=u[1], u[3] ,u[2]

        me = v
        if v not in take_node :
            if info[v] == 0 :
                sheep +=1
            elif info[v] ==  1 :
                wolf +=1
            if sheep <= wolf : sheep = 0
            take_node.append(v)
            take_node.sort()
            
            
        new_state = (tuple(take_node) ,me ,wolf , sheep)
        adj_list.append(new_state)
    return adj_list

def bfs(g,info):
    max_val = 1
    
    start=((0,),0,0,1)  
    parent = {start:None}
    level =[start]
    while len(level ) > 0  :
        new_level = []
        for u in level :
            for v in adj(u,g,info) :
                if v not in parent :
                    parent[v] = u
                    new_level.append(v)
                    max_val = max(max_val,v[3])
        level = new_level
    return max_val
#state :  0: 양,늑대 데려간 node 
#       1: 내 가 위치한 노드
#        2 : 늑대 개수
#       3 : 양 개수
def solution(info, edges):
    start = time.time()
    answer = 0
    all_state =[]
    g = {}
    for v in range(len(info)):
        g[v]= []
    for e in edges :
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    answer = bfs(g,info)    
    end= time.time()
    # print(f'time : {end-start}')
    # answer = max(all_state)
    
#     test

#     for k,v in g.items() :
#         print(f'vertex {k}  adjvertex {v}')

#   test adj
    # start=((0,),0,0,1)  
    # for k in adj(start , g,info) :
    #     print(k)
    return answer