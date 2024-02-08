# 보드에는 구멍이 하나 있다. 
# 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. O 
# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 
# 이때, 파란 구슬이 구멍에 들어가면 안 된다.

# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.  O 
# 각각의 동작에서 공은 동시에 움직인다 O 

# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다

# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 
# 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.  O 

# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.  O

# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램

# 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력  O 



# vertex : map의 state, 구슬들의 위치 

# edge : 기울이기 동작 4개 

# dest : red만 구멍안에 , 


N , M =list(map(int, input().split()))
board = []
red = None
blue= None
dest  = None
for i in range(N) :
    input_str = input()
    board.append([])
    for j in range(M) :
        ele = input_str[j]
        board[i].append(ele)
        if ele== 'R' :
            red= (i,j)
        elif ele == 'B' :
            blue = (i,j)
        elif ele == 'O' :
            dest= (i,j)

def indsafe(x,y) :
    if not(x >=0 and x<N and y>=0 and y<M) : return False
    if board[x][y] == '#' : return False
    return True
def move(marble,deltax,deltay) :
    marble_x,marble_y = marble[0] ,marble[1]
    while indsafe(marble_x+deltax,marble_y+deltay) :
        marble_x += deltax
        marble_y += deltay
        if (marble_x,marble_y) == dest :
            break
    
    return (marble_x,marble_y)
    
def adj(u) :
    adj_list = set()
    # print(u)
    temp_dict=  dict(u)
    if temp_dict['red'] == dest or temp_dict['blue'] == dest :
        # print('fire in the hole')
        return []
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    moving=[(min,1,-1),(max,1,1)  , (min,0,-1), (max,0,1)]
    indmap ={0:'red',1:'blue'}
    org_red ,org_blue = temp_dict['red'] , temp_dict['blue']
    
    
    
    
    for deltax,deltay,mov in zip(dx,dy,moving) :
        
        temp_red = move(org_red,deltax,deltay)
        temp_blue = move(org_blue,deltax,deltay)
        temp_dict = {'red':list(temp_red),'blue':list(temp_blue)}
        if temp_red == temp_blue and temp_red != dest : 
            funct , ind , delta  = mov
            temp_li = [org_red[ind],org_blue[ind]]
            delta_ind = temp_li.index(funct(temp_li))
            to_change = temp_dict[indmap[delta_ind]]
            temp_dict[indmap[delta_ind]][ind] +=  delta
            
        temp_dict['red'] = tuple(temp_dict['red'])
        temp_dict['blue'] = tuple(temp_dict['blue'])
    
        adj_list.add(tuple(temp_dict.items()))
    return list(adj_list)


def bfs(start,dest) :
    answer= -1
    parent={start:None}
    level =[[start]]
    
    while level[-1] and len(level) <11 :
        level.append([])
        for u in level[-2]  :
            for v in adj(u) :
                if v not in parent :
                    parent[v] = u
                    level[-1].append(v)
                    
        for state in level[-1] :
            # print(state)
            state  = dict(state)
            # print(state['red'] == dest and  state['blue'] != dest)
            if state['red'] == dest and state['blue'] != dest :
                answer = len(level) - 1 
                break
        else:
            continue
        break

    return answer , level
start = {}
start['red'] = red
start['blue'] = blue
start = tuple(start.items())
# print(bfs(start ,dest))
answer ,level = bfs(start,dest)

# print(level[1])
# print(level[1])
print(answer)
