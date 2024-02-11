# 카드 16장이 뒷면을 위로하여 4 x 4 크기의 격자 형태로 O
# 8가지의 캐릭터 그림이 그려진 카드가 각기 2장   O
#  무작위로 배치  O
# 유저가 카드를 2장 선택하여 앞면으로 뒤집었을 때                                                           같은 그림이 그려진 카드면 해당 카드는 게임 화면에서 사라지며     O
# 같은 그림이 아니라면 원래 상태로 뒷면이 보이도록 뒤집  O 
# 모든 카드를 화면에서 사라지게 하면 게임이 종료
# 카드는 커서를 이용해서 선택  커서: 유저가 선택한 현재 위치를 표시하는 "굵고 빨간 테두리 상자"


# 방향키 ←, ↑, ↓, → 중 하나를 누르면, 커서가 누른 키 방향으로 1칸 이동  O
# [Ctrl] 키를 누른 상태에서 방향키 ←, ↑, ↓, → 중 하나를 누르면, 누른 키 방향에 있는 가장 가까운 카드로 한번에 이동  O
#  [CTRL] 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동  O
# # 누른 키 방향으로 이동 가능한 카드 또는 빈 공간이 없어 이동할 수 없다면 커서는 움직이지 않습니다.  O

# 커서가 위치한 카드를 뒤집기 위해서는 [Enter] 키를 입력  O
# [Enter] 키를 입력해서 카드를 뒤집었을 때 O  
# 앞면이 보이는 카드가 1장 뿐이라면 그림을 맞출 수 없으므로 두번째 카드를 뒤집을 때 까지 앞면을 유지합니다.  O
# 앞면이 보이는 카드가 2장이 된 경우, 두개의 카드에 그려진 그림이 같으면 해당 카드들이 화면에서 사라지며, 그림이 다르다면 두 카드 모두 뒷면이 보이도록 다시 뒤집힙니다. O

#  키 조작 횟수는 방향키와 [Enter] 키를 누르는 동작을 각각 조작 횟수 1로 계산하며   O
# Ctrl] 키와 방향키를 함께 누르는 동작 또한 조작 횟수 1로 계산합니다.  O

# 배열의 각 원소는 0 이상 6 이하인 자연수  
# 0은 카드가 제거된 빈 칸
#  부터 6까지의 자연수는 2개씩 들어있으며 같은 숫자는 같은 그림의 카드를 의미
# 뒤집을 카드가 없는 경우(board의 모든 원소가 0인 경우)는 입력으로 주어지지 않습니다.
# r은 커서의 최초 세로(행) 위치를 의미합니다.
# c는 커서의 최초 가로(열) 위치를 의미합니다.
# r과 c는 0 이상 3 이하인 정수입니다.
# 게임 화면의 좌측 상단이 (0, 0), 우측 하단이 (3, 3) 입니다.

board_size  = 4

def indchk(x,y) :
    return x>=0 and x <board_size and y>=0 and y< board_size


def not_remain_card(x,y,u) :
    # print(f'rematin test : {u}')
    for i in range(1,7) :
        # pass
        for c in u[i]  :
            # pass
            if c == (x,y) :
                return False
    return True
def ctrl_move(org_cursor,dx,dy,u) :
    x , y = org_cursor
    while indchk(x+dx,y+dy) and not_remain_card(x+dx,y+dy,u):
        x ,y  = x+dx , y+dy
        
        
    if indchk(x+dx,y+dy)  : 
        
        # print('card detect')
        x , y = x+dx, y+dy
        
    return (x,y)
        

def move(org_cursor,dx,dy) :
    x , y = org_cursor
    if indchk(x+dx,y+dy) :
        x , y = x+dx , y+dy
    return (x,y)

def card_check(cursor,card_list) :
    for i in range(1,7)  :
        for card in card_list[i] :
            if card == cursor :
                return i
    return 0

def card_len(card_list) :
    ans = 0
    for i in range(1,7)  :
        ans += len(card_list[i])
            
    return ans
def adj(u,board) :
    adj_list = []
    temp_u= dict(u)
    u  = dict(u)
    org_cursor = u['cursor']
    # flip_card =  u['flip']
    
    deltax= [0,0,1,-1]
    deltay = [1,-1,0,0]
    cursor_set = set()
    for dx,dy in zip(deltax,deltay) :
        new_cursor = move(org_cursor,dx,dy)
        cursor_set.add(new_cursor)
        new_cursor = ctrl_move(org_cursor,dx,dy,u)
        cursor_set.add(new_cursor)
    # print(cursor_set)
    card_num = card_check(org_cursor,u)
    # temp_u = dict(tuple(u.items())
    if card_num >0 :
        if len(temp_u['flip']) == 0 : 
            x,y = org_cursor
            temp_u['flip'] = (card_num,x,y)
            temp_list = []
            for  c in temp_u[card_num]  :
                if c !=org_cursor  :
                    temp_list.append(c)
                    temp_list.sort()
            temp_u[card_num] = tuple(temp_list)
#             if card_len(temp_u) %2 == 0 : 
                
#                 print('flip 빈거 error')
#                 # print(f'cursor :{x,y}')
#                 # print(f'level  :{count}')
#                 print(temp_u)
                
        else :
            flip_num ,flip_x,flip_y = temp_u['flip'][0] , temp_u['flip'][1] ,temp_u['flip'][2]
            if flip_num == card_num  :
                # temp_list = []
                # for c in temp_u[card_num] :
                #     if c !=org_cursor  :
                #         temp_list.append(c)
                #         temp_list.sort()
                temp_u[card_num] = ()
                temp_u['flip']   = ()
                # if card_len(temp_u) % 2 != 0 : 
                #     print('같은거 error')
                #     print(card_len(temp_u))
                #     print(temp_u)
            else :
                temp_list = list(temp_u[flip_num] )
                temp_list.append((flip_x,flip_y))
                temp_u[flip_num]  = tuple(temp_list)
                temp_u['flip']   = ()
                # if card_len(temp_u) % 2 != 0 :
                #     print('다른거 error')
                #     print(temp_u)
                # if not temp_u[fli]
    adj_list.append(tuple(temp_u.items()))
    for c in cursor_set :
        u['cursor'] = c
        adj_list.append(tuple(u.items()))
    return adj_list

def bfs(board ,start) :
    
    parent={start :None}
    level = [start]
    answer = -1
    count =0
    while len(level) >0   :
        count+=1
        new_level = []
        for u in level :
            for v in adj(u,board) :
                if v not in parent :
                    parent[v] = u
                    new_level.append(v)
        level = new_level    
        for state in level :
            state = dict(state)
            # if count == 4 :
            #     if not state[2] :
            #         print(state)
            for i in range(1,7) :
                if state[i] : break
            else :
                answer = count
                # print('answer_state')
                # print(state)
                break
        else :
            continue
        break
    # print(count)
    # pass
    return answer
    
    
# state : 커서위치 , 남은카드
def solution(board, r, c):
    answer = 0
    start = {}
    for i in range(1,7):
        start[i] = []
    start["cursor"] = (r,c)
    start["flip"]  =()
    # start['remain'] = tuple([()])
    # start["del"] = set()
    for x in range(len(board)):
        for y in range(len(board)) :
            if board[x][y] == 0 : continue
            start[board[x][y]].append((x,y))
    for i in range(1,7)         :
        start[i] = tuple(start[i])
    
    start = tuple(start.items())
    # print(start)
    # start =  dict(start)
    # print(start)
    # print(start)
#     deltax= [0,0,1,-1]
#     deltay = [1,-1,0,0]
#     print('1칸')
#     for dx,dy in zip(deltax,deltay) :
#         print(move((r,c)  ,dx,dy))
        
#     print('ctrl')
#     for dx,dy in zip(deltax,deltay ):
#         print(ctrl_move((r,c)  ,dx,dy , board))
    # for a in adj(start,board) :
    #     print(a)
    
    answer= bfs(board,start)
    return answer