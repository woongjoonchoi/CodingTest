board_size = 4

def indchk(x,y) :
    return x>=0 and x< board_size and y>=0 and y<board_size
def state_check(state,r,c) :
    for i in range(1,7) :
        for t in state[i] :
            if t == (r,c) :
                return i
    return 0
def board_making(state) :
    new_board= [ [0 for _ in range(board_size)] for _ in range(4)]
    for i in range(1,7) :
        for r,c in state[i] :
            new_board[r][c] = i
    return new_board
def adj(u,board):

    state = dict(u)
    adj_li = []
    r,c = state["pos"]
    temp_set =set()
    board_color = state_check(state,r,c)  
    if board_color !=0 : ## 틀린부분
        li = []
        for   p in list(state[board_color]) :
            if p != (r,c) : 
                li.append(p)
                break
        if  not state["flip"] :
            state["flip"] = tuple([(board_color ,r,c)])
            state[board_color] =tuple(li)
        else :
            card_val , f_r,f_c = state["flip"][0]  
            if card_val == board_color :
                state[board_color] = tuple(li)
            else : 
                temp_list = list(state[card_val])
                temp_list.append((f_r,f_c))
                temp_list.sort()
                state[card_val] = tuple(temp_list)
                board[f_r][f_c] = card_val
            state["flip"] = tuple([])
        temp_set.add(tuple(state.items()) )
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for deltax ,deltay in zip(dx,dy) :
        new_state = dict(u)
        new_r,new_c = r+deltax,c+deltay
        if not indchk(new_r,new_c) :    ## 틀린부분 adj
            new_r ,new_c= r , c
        new_state["pos"] =(new_r,new_c)
        temp_set.add(tuple(new_state.items()))
        temp_x,temp_y = r,c
        new_state=dict(u)
        temp_board =  board_making(new_state)#틀린부분
        while indchk(temp_x+deltax,temp_y+deltay) :
            temp_x +=deltax
            temp_y += deltay
            if temp_board[temp_x][temp_y] != 0 :
                break
        new_state["pos"] = (temp_x,temp_y)
        temp_set.add(tuple(new_state.items()))
    adj_li = list(temp_set)
    return adj_li
def print_path(parent,v):
    node = v
    while node is not None :
        print(node)
        node = parent[node]
## 0: pos, 1~6 : card number
def bfs(start,board):
    parent = {start:None}
    level = [[start]]
    answer_found = False
    count =0
    while level :
        level.append([])
        if len(level) == 11 :
            print('hi')
        for u in level[-2] :
            for v in adj(u,board) :
                if v not in parent :
                    level[-1].append(v)
                    parent[v] = u
        for u in level[-1] :
            temp_dict = dict(u)
            for i in range(1,7) :
                if   temp_dict[i]: break  # 틀린부분
            else :
                break
            continue
        else :
            continue
        break
    return level
def solution(board, r, c):
    answer = 0
    start = {}
    start["pos"] = (r,c)
    start["flip"] =()
    for i in range(1,7) :
        start[i] = []
    for x in range(len(board )):
        for y in range(len(board)) :
            if board[x][y] !=0 :
                start[board[x][y]].append((x,y))
    for i in range(1,7) :
        start[i] = tuple(start[i])
           
    lev = bfs(tuple(start.items()),board)

    answer = len(lev) -1
    return answer

print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]],1,0))