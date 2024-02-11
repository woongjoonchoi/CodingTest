board_size = 4

def indchk(x,y) :
    return x>=0 and x< board_size and y>=0 and y<board_size

def adj(u,board):

    state = dict(u)
    adj_li = []
    r,c = state["pos"]
    if board[r][c] !=0 :
        li = []
        for   p in list(state[board[r][c]]) :
            if p != (r,c) : 
                li.append(p)
                break
        state[board[r][c]] =tuple(li)
        
        adj_li.append(tuple(state.items()))
    # print(f"after u:{u}")
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    temp_set = set()
    for deltax ,deltay in zip(dx,dy) :
        if not indchk(r+deltax,c+deltay) : continue
        temp_set.add((r+deltax,c+deltay))
        temp_x,temp_y = r,c
        while indchk(temp_x+deltax,temp_y+deltay) :
            temp_x +=deltax
            temp_y += deltay
        temp_set.add((temp_x,temp_y))

    for new_r,new_c in temp_set :
        if (r,c) == (new_r,new_c) : continue
        new_state = dict(u)
        new_state["pos"] = (new_r,new_c)
        adj_li.append(tuple(new_state.items()))
    # adj_li.append(list(temp_set))
        
    return adj_li
    # pass
    

    
## 0: pos, 1~6 : card number
def bfs(start,board):
    parent = {start:None}
    level = [[start]]
    answer_found = False
    while level :
        level.append([])
        # if len(parent) >100000 : 
        #     pass
        #     print(len(parent))
        for u in level[-2] :
            for v in adj(u,board) :
                if v not in parent :
                    level[-1].append(v)
                    parent[v] = u
        # if len(level) ==14 :
        #     print('hi')
        for u in level[-1] :
            temp_dict = dict(u)
            for i in range(1,7) :
                if   temp_dict[i] : break
            else :
                break
            continue
        else :
            continue
        break
        
    return level
                

def solution(board, r, c):
    answer = 0
    
    test_key = {}
    test_key["pos"] = (r,c)
    test_key["1"] = [(2,3)]
    test_key["1"].append((4,5))
    # print(tuple(test_key.items()) == 	(('pos', (0, 1)), ('1', [(2, 3), (4, 5)])))
    # di={}
    # print(tuple(test_key.items()))
    di = dict(tuple(test_key.items()))
    # di[tuple(test_key.items())]  = 4
    # print()
    # print(di)
    # print(tuple(di.items()))
    
    test_key={}
    test_key["pos"] = (r,c)
    test_key[3] =((0,3),(3,0))
    test_key[2] = ((1,0),(2,3))
    test_key[1] = ((0,0) , (3,2))
    # temp_set = set()
    # temp_set.add(tuple(test_key.items()))
    # print(adj(tuple(test_key.items()) , board))
    
    # a=[(0,0) , (3,2)]
    # print(tuple(a))
    # print(dict(tuple(test_key.items())))
    # for k in adj(tuple(test_key.items()) , board):
    #     print(k)
    start = {}
    start["pos"] = (r,c)
    for i in range(1,7) :
        start[i] = []
    for x in range(len(board )):
        for y in range(len(board)) :
            if board[x][y] !=0 :
                start[board[x][y]].append((x,y))
    for i in range(1,7) :
        start[i] = tuple(start[i])
           
    # print(start)
    lev = bfs(tuple(start.items()),board)
    
    print(len(lev))
    print(lev[0])
    for l in lev[13]:
        print(l)
        print('--------------')
    # print(tuple(start.items()) == 	(('pos', (0, 1)), (1, ((1, 2), (2, 1))), (2, ((0, 3), (3, 0))), (3, ((0, 0), (3, 3))), (4, ()), (5, ()), (6, ())))
    # print(adj(tuple(start.items()) ,board))
    # level = [[]]
    # tup_start= tuple(start.items())
    # parent={tup_start:None}
    # for v in adj(tup_start,board) :
    #     if v not in parent :
    #         level[-1].append(v)
    #         parent[v] = tup_start
    # start = {}
    # start["pos"] = (r,c)
    # for i in range(1,7) :
    #     start[i] = (())
    # level = [[tuple(start.items())]]    
    # while  1:
    #     for u in level[-1] :
    #         print(u)
    #         temp_dict = dict(u)  ## 틀린부분
    #         print(temp_dict)
    #         for i in range(1,7) :
    #             print(f'u[i] : {temp_dict[i]}')
    #             print(f'len u[i] : {len(temp_dict[i])}')
    #             if not temp_dict[i]  : continue
    #             break
    #         else :
    #                     break
    #         continue
    #     else :
    #         continue
    #     break
    # # print(parent.keys())
    return answer

# di={}
# di[3] = [4]
# di[2] = [5,6]

# print(len(di))
print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]],1,0))