# 8가지의 캐릭터 그림이 그려진 카드가 각기 2장씩 화면에 무작위로 배치되어 있습니다.


# 카드는 커서를 이용해서 선택
# 커서는 4 x 4 화면에서 유저가 선택한 현재 위치를 표시하는 "굵고 빨간 테두리 상자"를 의미합니다.
# 


# 방향키 ←, ↑, ↓, → 중 하나를 누르면, 커서가 누른 키 방향으로 1칸 이동 O

# [Ctrl] 키를 누른 상태에서 방향키 ←, ↑, ↓, → 중 하나를 누르면, 누른 키 방향에 있는 가장 가까운 카드로 한번에 이동
# 만약, 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동
# 누른 키 방향으로 이동 가능한 카드 또는 빈 공간이 없어 이동할 수 없다면 커서는 움직이지 않습니다.



# 커서가 위치한 카드를 뒤집기 위해서는 [Enter] 키를 입력 O
# [Enter] 키를 입력해서 카드를 뒤집었을 때 O
# 앞면이 보이는 카드가 1장 뿐이라면 그림을 맞출 수 없으므로 두번째 카드를 뒤집을 때 까지 앞면을 유지 O

# 앞면이 보이는 카드가 2장이 된 경우,   O
# 두개의 카드에 그려진 그림이 같으면 해당 카드들이 화면에서 사라지며, O
# 그림이 다르다면 두 카드 모두 뒷면이 보이도록 다시 뒤집힙니다. O

# 남은 카드를 모두 제거하는데 필요한 키 조작 횟수의 최솟값



# 앞면인 카드를 다시 뒤집을 수는 없다. 여기서 30분해맴


# 앞면 비교할때 board[r] ->  board[r][c]
import copy

def check_safe(x,y) :
    return x>=0 and x<4 and y>=0 and y< 4

def adj(u) :
    temp_u = dict(u)

    adj_list = []
    r,c  =  temp_u['cursor'] 
    
    board = [list(ele) for ele in temp_u['board']]
    flip =temp_u['flip']
    # return
    if board[r][c] !=0 and (board[r][c],r,c) !=flip   :
        # if (r,c) == (0,0) :
            # print(f'board[r] : {board[r]})
        if isinstance(flip,tuple) : 
            if board[r][c] == flip[0] :
                board[r][c] =0
                board[flip[1]][flip[2]] =0
                
            flip=0
        else :
            flip = (board[r][c],r,c)
            # board[r][c] = 0
        temp_u['board']= tuple(tuple(ele)for ele in board)
        temp_u['flip'] = flip
        adj_list.append(tuple(temp_u.items()))
    
    deltax = [0,0,1,-1]
    deltay = [1,-1,0,0]
    temp_u = dict(u)
    r,c  = temp_u['cursor']
    board=temp_u['board']

    for dx,dy in zip(deltax,deltay) :
        if check_safe(r+dx,c+dy) :
            temp_u['cursor'] = r+dx,c+dy
        else :
            temp_u['cursor'] = r,c
        adj_list.append(tuple(temp_u.items()))
        
        
    for dx,dy in zip(deltax,deltay) :
        new_r ,new_c = r,c
        while check_safe(new_r+dx,new_c+dy) and board[new_r+dx][new_c+dy] == 0 :
            new_r,new_c = new_r+dx,new_c+dy
        if check_safe(new_r+dx,new_c+dy)  and board[new_r+dx][new_c+dy] !=0 :
            new_r,new_c = new_r+dx,new_c+dy
        temp_u['cursor'] = new_r,new_c
        adj_list.append(tuple(temp_u.items()))
    return adj_list

                

def bfs(start):
    answer = 0
    end = tuple((0,0,0,0) for _ in range(4))
    parent={start:None}
    
    level = [start]
    depth =0
    dest = None
    while level :
        new_explore= []
        depth+=1
        for u in level :
            for v in adj(u) :
                if v not in parent :
                    parent[v] = u
                    new_explore.append(v)
                    if dict(v)['board'] == end :
                        print(dict(v))
                        dest= v
                        break
            else:
                continue
            break
        else :
            level= new_explore
            continue
        break
    # count = depth
    # while dest :
    #     print(f'count :{count}')
    #     print(dest)
    #     dest = parent[dest]
    #     count-=1
    answer= depth
    return answer

def solution(board, r, c):
    answer = 0
    start = {}
    start['flip'] = 0
    start['cursor'] = (r,c)
    start['board'] = copy.deepcopy(board)
    start['board'] =tuple(tuple(ele) for ele in start['board']  )

    answer = bfs(tuple(start.items()))
    
    # print((board[0],0,0) != (1, 0, 0))
    return answer