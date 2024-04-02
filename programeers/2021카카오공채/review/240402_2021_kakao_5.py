
# 게임이 시작되면 화면에는 카드 16장이 뒷면을 위로하여 4 x 4 크기의 격자 형태로 표시되어 있습니다.

#  각 카드의 앞면에는 카카오프렌즈 캐릭터 그림이 그려져 있으며, 8가지의 캐릭터 그림이 그려진 카드가 각기 2장씩 화면에 무작위로 배치되어 있습니다.


# 유저가 카드를 2장 선택하여 앞면으로 뒤집었을 때 같은 그림이 그려진 카드면 해당 카드는 게임 화면에서 사라지며, 같은 그림이 아니라면 원래 상태로 뒷면이 보이도록 뒤집힙니다 


# 카드는 커서를 이용해서 선택할 수 있습니다.
# 커서는 4 x 4 화면에서 유저가 선택한 현재 위치를 표시하는 "굵고 빨간 테두리 상자"를 의미합니다. 


# 커서는 [Ctrl] 키와 방향키에 의해 이동되며 키 조작법은 다음과 같습니다.
# 방향키 ←, ↑, ↓, → 중 하나를 누르면, 커서가 누른 키 방향으로 1칸 이동합니다.
# [Ctrl] 키를 누른 상태에서 방향키 ←, ↑, ↓, → 중 하나를 누르면, 누른 키 방향에 있는 가장 가까운 카드로 한번에 이동합니다.
# 만약, 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동합니다.
# 만약, 누른 키 방향으로 이동 가능한 카드 또는 빈 공간이 없어 이동할 수 없다면 커서는 움직이지 않습니다.

# 커서가 위치한 카드를 뒤집기 위해서는 [Enter] 키를 입력합니다.
# [Enter] 키를 입력해서 카드를 뒤집었을 때
# 앞면이 보이는 카드가 1장 뿐이라면 그림을 맞출 수 없으므로 두번째 카드를 뒤집을 때 까지 앞면을 유지합니다.
# 앞면이 보이는 카드가 2장이 된 경우, 두개의 카드에 그려진 그림이 같으면 해당 카드들이 화면에서 사라지며, 그림이 다르다면 두 카드 모두 뒷면이 보이도록 다시 뒤집힙니다.


# "베로니"는 게임 진행 중 카드의 짝을 맞춰 몇 장 제거된 상태에서 카드 앞면의 그림을 알고 있다면, 남은 카드를 모두 제거하는데 필요한 키 조작 횟수의 최솟값을 구해 보려고 합니다. 
# 키 조작 횟수는 방향키와 [Enter] 키를 누르는 동작을 각각 조작 횟수 1로 계산하며, [Ctrl] 키와 방향키를 함께 누르는 동작 또한 조작 횟수 1로 계산합니다.

# state :  커서위치 , 남은카드위치(보드)  , 앞면뒷면
import copy
import typing
def indchk(x,y) :
    
    return x>=0 and x<4 and y>=0 and y<4
def adj(v) :
    temp_v = dict(v)
    cursor,rem,front = temp_v['cursor'],temp_v['rem'],temp_v['front']
    x,y = cursor
    deltax=[1,-1,0,0]
    deltay  = [0,0,1,-1]
    adj_list = []
    for dx,dy in zip(deltax,deltay):
        if not indchk(dx+x,dy+y) : continue
        temp_v['cursor'] = (dx+x,dy+y)
        adj_list.append(tuple(temp_v.items()))
    for dx,dy in zip(deltax,deltay) :
        temp_x ,temp_y= x,y
        while indchk(dx+temp_x,dy+temp_y) :
            temp_x +=dx
            temp_y +=dy
            if  rem[temp_x][temp_y]  :
                break
        temp_v['cursor'] = (temp_x,temp_y)
        adj_list.append(tuple(temp_v.items()))
    temp_v['cursor'] = (x,y)
    if rem[x][y] and (isinstance(front,int) or front[1:] != (x,y) )    :
    # if rem[x][y]    :
        if front ==0 :
            temp_v['front'] = (rem[x][y],x,y)
        elif rem[x][y] == front[0] :
            rem = list( list(r) for r in rem)
            rem[x][y] = 0
            rem[front[1]][front[2]] = 0
            rem = tuple(tuple(r) for r in rem)
            temp_v['rem'] = rem
            temp_v['front'] = 0
        elif rem[x][y] != front[0] :
            temp_v['front'] = 0
        adj_list.append(tuple(temp_v.items()))
            
    return adj_list
            

def bfs(state) :
    
    parent ={state : None}
    level = [state]
    depth = 0
    answer = tuple((0,0,0,0) for _ in range(4))
    dest = None
    count= 0
    while len(level) > 0 :
        new_explore = []
        depth +=1
        for v in level :
            for u in adj(v) :
                if u not in parent :
                    parent[u] =v
                    new_explore.append(u)
                    if dict(u)['rem'] == answer :
                        dest = u
                        # print(dest)
                        break
            else :
                continue
            break
        else :
            level = new_explore 
            # print(f'depth :{depth}')
            # print(len(level))
            continue
        break
    levels  = depth
    # while dest is not None :
    #     print(f'level : {levels}')
    #     print(dest)
    #     dest = parent[dest]
    #     levels-=1
    # print('hi')
    return depth
        
def solution(board, r, c):
    answer = 0
    state = {}
    rem_card = tuple(tuple(b)  for b in board )
    front = 0
    state['cursor'] = (r ,c)
    state['rem'] = rem_card
    state['front'] = front
    state = tuple(state.items())
    # print(state[1][1])
    # print(isinstance(state,typing.Hashable))
    # answer = tuple((0,0,0,0) for _ in range(4))
    # print(answer)
    # print(isinstance(state,typing.Hashable))
    # print(adj(state))
    # for vv in adj(state):
    #     print(vv)
    
    
    answer= bfs(state)
    # state = dict(state)
    # state['front']  = (2,0,1)
    # for vv in adj(tuple(state.items())) :
    #     print(vv)
    # ab = (1,2,3)
    # print(ab[1:])
    return answer