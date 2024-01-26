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
def adj(u) :
    dx= [0,0,1,-1]
    dy =[1,-1,0,0]
    ans = []
    for i in range(4) :
        adj_i = u[0] + dx[i]
        adj_j = u[1] + dy[i]
        if not(adj_i >=0 and adj_i < N and adj_j >=0 and adj_j < M ) or board[adj_i][adj_j] =='#'  : continue
        
        ans.append( [[adj_i,adj_j] , [dx[i],dy[i]] ])
        
    return ans
        
def bfs(s) :
    parent[s[0]][s[1]] = None
    level = [[s]]
    while 0 < len(level[-1]) :
        level.append([])
        for u in level[-2] :
            for v,_ in adj(u) :
                if parent[v[0]][v[1]] is None :
                    parent[v[0]][v[1]] = u
                    level[-1].append(v)
    
def move(direct,cp,red,blue) :
    org_blue = blue[:]
    i = blue[0]+direct[0]
    j = blue[1]+direct[1]  
    while i>=0 and i<N and j>=0 and j<M :
        if board[i][j] == '#' :
            break
        blue[0] = i
        blue[1] = j
        if board[blue[0]][blue[1]] == 'O' :
            return -1
        i = blue[0]+direct[0]
        j = blue[1]+direct[1]
        
    if blue[0] != cp[0] or blue[1] != cp[1] : return 1
    
    if direct[1] == -1 :
        if red[1] < org_blue[1] :
            blue[1] +=1
        elif red[1] > org_blue[1] :
            red[1] +=1
            
    elif direc[1] == 1 :
        if red[1]  > org_blue[1] :
            blue[1] -=1
        else :
            red[1] -=1 
    elif direc[0] == 1 :
        if red[0] <org_blue[0] :
            blue[0] +=1
        else :
            red[0] +=1
    elif direc[0] == -1 :
        if red[0] >org_blue[0] :
            blue[0] -=1
        else :
            red[0] -=1
    # if change_point
    return 1

def short_path():
    i= dest
    path = [dest]

    while i != red :
        i = parent[i[0]][i[1]]
        path.append(list(i))
    return path


parent =[ [None for _ in range(M)] for _ in range(N)]
answer = 0
test_condition = True

while test_condition:
    bfs(red)
    # print(f'source : {red} , dest: {dest} ,blue :{blue}')
    if parent[dest[0]][dest[1]] is None :
        test_condition =False
        answer=  -1
        # print(f'no path to dest')
        break
    path = short_path() 
    direc=  [[-1,-1]]  # direc : bfs에서의 진행방향  ,generality를 위해 초기값 
    count = 0  # 방향이 꺽일때마다 count ,예비 answer

    change_point = []  # 방향이 꺽이는지점
    for k in range(len(path)-1,0,-1) :
        delta_x = path[k-1][0] - path[k][0] 
        delta_y = path[k-1][1] - path[k][1] 
        if delta_x !=direc[-1][0] or delta_y != direc[-1][1] :
            count +=1
            direc.append([delta_x ,delta_y])
            change_point.append(path[k])
    change_point.append(dest)


    t = len(direc) -1  # direc inddex
    k = 1  # change_point index
    temp_r = red[:]
    temp_b = blue[:]
    while t>0 :
        temp_r = change_point[k]
        if move(direc[t],change_point[k],temp_r,temp_b) == -1 :
            answer = -1
            test_condition = False
            # print(f"blue ball fisrt escape")
            break
        t-=1
        k+=1
        answer+=1
    
    blue = temp_b
    red= temp_r
    if answer >10 : 
        test_condition =False
        # print(f"more than 10")
        answer= -1
    if red[0] == dest[0] and red[1] == dest[1] :
        # print(f'red :{red} ball go to dest :{dest} ')
        break
    
    i = dest
    while i != red :
        temp_i = i
        i = parent[i[0]][i[1]] 
        parent[temp_i[0]][temp_i[1]] = None


    
print(answer)