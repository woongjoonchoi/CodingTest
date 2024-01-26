## 문제에 대한간략한 증명


### vertex : 기울이고 난 후의 map
### vertex 의 degree max : 4

### vertex의 upper bound : 81 C 2

### edge의 upper bound : 4 * 81 C 2

### BFS의 upper bound O(V+E) <  5 * 81 C 2  -> 약 2만~3만 



N, M  = list( map(int,input().split()))


board ,blue,red,dest= [] , None,None,None

for i in range(N) :
    board.append(list(input()))
    
for i in range(N) :
    for j in range(M) :
        if board[i][j]== 'R' :
            red = [i,j]
        elif board[i][j] == 'B' :
            blue = [i,j]
            
        elif board[i][j] == 'O' :
            dest =(i,j)
            


# def check(chk,blue,red) :  ##  blue,red가 같은 열 혹은 행에 있는지 확인   
#     a =1
#     for c , b , r in zip(chk,blue,red) :
#         a *= c * b == c*r
#     return a

def same_check(blue,red) :
    for b,r in zip(blue,red) :
        if b!= r :
            return 0
    else :
        return 1
def go_wall_or_escape(x,y,board,d) :
    escape = 0
    
    while board[x+d[0]][y+d[1]] != '#'  and board[x+d[0]][y+d[1]] != 'O':
        x +=d[0]
        y += d[1]
    if board[x+d[0]][y+d[1]] == 'O' :
        x +=d[0]
        y += d[1]
    return [x , y]
        
def element_wise(li_a,li_b) :
    return sum([a*b for a,b in zip(li_a,li_b)])
        
def neighbor(board , blue,red) :
    
    direction = [(0,1),(0,1) ,(1,0),(1,0)]  # 북남 동서 같은 줄에 위치한지 체크용
    
    delta =[(-1,0),(1,0) , (0,1) ,(0,-1)]  # 북 남 동 서 
    
    # start = [[]]
    new_ans = []
    # print(f'org_blue :{blue} ,org_red:{red}')
    for chk , d in zip(direction,delta) :
        
        # if check(chk,blue,red)  : flag =True
        temp_blue = go_wall_or_escape(blue[0],blue[1],board,d)
        temp_red = go_wall_or_escape(red[0],red[1],board,d)
        # print(f'temp_blue :{temp_blue}  ,temp_red:{temp_red}')
        # if check(chk,temp_blue,temp_red) :
        if same_check(temp_blue,temp_red) : 
            if not( dest[0] == temp_blue[0] == temp_red[0] and 
                   dest[1] == temp_blue[1] == temp_red[1] ):
                tempo = [temp_blue,temp_red]
                li = [element_wise(blue,d),element_wise(red,d)]
                min_ind = li.index(min(li))
                tempo[min_ind][0]  += -1* d[0]
                tempo[min_ind][1]  += -1 * d[1]
        # print(f'changed ! temp_blue :{temp_blue}  ,temp_red:{temp_red}')
        for r,org_r,b,org_b in zip(temp_red,red,temp_blue,blue)  :
            if r != org_r or b !=org_b :  
                break
        else :
            continue
        new_ans.append([temp_blue,temp_red])
        
    return new_ans
        
def path_length(parent) :
    # start = dest
    start  = None
    for k in parent.keys() :
        if tuple(k[1]) == tuple(dest) :
            start = k
            break
        
    # print(f'start : {start}')
    # print(f'blue :{blue}  red: {red}')
    # print(f'parent keys : {parent.keys()} ')
    path_len = 0
    while not same_check(start[0],blue) or  not same_check(start[1],red) : 
        start  = parent[(tuple(start[0]) ,tuple(start[1]))]
        path_len+=1
    return path_len

def solve_map() :
    
    parent , to_explore = {(tuple(blue),tuple(red)): None} , [(blue,red)]
    
    only_blue ,only_red = set() ,set()
    only_blue.add(tuple(blue))
    only_red.add(tuple(red))
    tup_dest = tuple(dest)
    depth = 0
    levels=[to_explore]
    
    
    while  to_explore  and depth <10: ## blue에 들어가는 state와 red에만 들어가는 state가 source로
                                        ## 부터 갈수있는 모든 config에 포함될 수 있다. 
        for k in to_explore : 
            only_blue.add(tuple(k[0]))
            only_red.add(tuple(k[1]))
        to_explore = bfs(to_explore,parent)
        levels.append(to_explore)    
        depth+=1    
    # print(f'level :{len(levels)}')
    answer = -1
    for i , l in enumerate(levels) :
        for k in levels[i] :
            if k[0] != tup_dest and k[1] == tup_dest :
                answer = i      
                # print(f'answer : {k}')
                break
        else :
            continue
        break
        
    # if  tup_dest in only_blue or tup_dest not in only_red: 
    #     # print(f'no path to source or path to blue hole')
    #     answer =-1
    # else : 
    #     # print(f'path to source exist')
    #     answer = path_length(parent)
    # if answer >10 : answer  = -1
    return answer 
def bfs(to_explore,parent) :
    
    new_explore = []
    for u in to_explore :  
        if u[0] == tuple(dest) or u[1] == tuple(dest) : ## 둘중 하나가 구멍에 빠지면 인접노드를 고려할 필요가 없다.
                                                        ## 하지만, state중 하나인건 분명하다. 
            continue
        for v in neighbor(board,u[0],u[1]) : # v[0]  :blue, v[1] : red
            tup_blue ,tup_red =tuple(v[0]) , tuple(v[1])
            if (tup_blue,tup_red) not in parent : 
                parent[(tup_blue,tup_red)] = (u[0] ,u[1])
                new_explore.append((tup_blue,tup_red))
    return new_explore
    
    
    
print(solve_map())

# adb= neighbor(board,blue,red)
# # print( type(True * True))


# for  k,v in adb :
    
#     print(f'new_blue:{k}  new_red:{v}')
