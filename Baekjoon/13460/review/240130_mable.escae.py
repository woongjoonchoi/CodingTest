N ,M = list( map(int,input().split()) )

board = []

red = None

blue = None

dest = None

for _ in range(N) :
    
    board.append(list(input()))
    
for x in range(N):
    for y in range(M) :
        if board[x][y] == 'R' :
            red = (x,y)
            
        elif board[x][y] == 'B' :
            blue = (x,y)
            
        elif board[x][y] == 'O' :
            dest = (x,y)
def indchk(x,y):
    limit_x = N
    limit_y = M
    
    return x >=0 and x< N and y>=0 and y<limit_y

def cord_change(x,y,d_x,d_y) :
    # print(f"x :{x} y {y}  d_x {d_x}  d_y {d_y}")
    # print(d_x)
    count = 0
    while indchk(x+d_x,y+d_y) :
        count+=1
        # print(f'loop_count :{count}')
        
        x += d_x
        y += d_y
        if board[x][y] == '#' :
            x -=d_x
            y -=d_y
            break
        elif board[x][y] == 'O' :
            break
    return x,y
def move(u,dx,dy)   :

    ans = []
    for d_x,d_y in zip(dx,dy) :
        red ,blue  = u 
        # if not isinstance(red  ,tuple) : print(f'u : {u}')
        red_x ,red_y  = red
        blue_x,blue_y = blue

        new_red = cord_change(red_x,red_y,d_x,d_y)
        new_blue = cord_change(blue_x,blue_y,d_x,d_y)
        
        # print(f'new_red :{new_red}  ,new_blue :{new_blue}')
        ans.append((new_red,new_blue))
    
    return ans

def adjust(u,c,deltax,deltay) :
    red,blue = c
    red,blue = list(red),list(blue)
    temp_list = [red,blue]
    org_red,org_blue= u

    r_cord = deltax *org_red[0] + deltay * org_red[1]
    b_cord= deltax *org_blue[0] + deltay * org_blue[1]
   
    li = [r_cord,b_cord]
    change_ind = li.index(min(li))
    # print(f'change_ind :{change_ind}')
    temp_list[change_ind][0] += -1 * deltax
    temp_list[change_ind][1] += -1 * deltay
    c= (tuple(temp_list[0] ) ,tuple(temp_list[1]))
    return c
    
def adj(u,start):
    dx =[0,0,1,-1]
    dy = [1,-1,0,0]

    candi = move(u,dx,dy)

    masking = [True] * 4
    ans = []
    # print(f'candi : {candi}')
    for i , c in enumerate(candi) :
        if c == u : continue
        elif c[0] == c[1] : 
            if c[0] == dest :  
                ans.append(c)
                continue
            
            k = adjust(u,c, dx[i],dy[i])
            if k == u : continue
            ans.append(k)
            
        else : 
            ans.append(c)
    return ans
            
            
def bfs() :
    
    parent = {}
    start = (red,blue)
    parent[start] = None 
    
    level = [[start]]  ## 틀린부분
    # print(level)
    while 0 < len(level[-1]) and len(level) < 11 :  ## 틀린부분 or
        level.append([])
        
        for u in level[-2] :
            # if u[0] == u[1] and u[0] ==  dest : continue #틀린부분
            if u[1] ==  dest or u[0] == dest : continue # 또틀린 부분
            for v in adj(u,start) :
                
                if v not in parent :
                    level[-1].append(v)
                    parent[v] = u
    return level

levels = bfs()

answer = None
for i, l in enumerate(levels) :
    for r,b in l :
        if r == dest and b!= dest : 
            answer = i
            break
    else :
        continue
    break

if answer is None : answer = -1
print(answer)
# print(len(levels))
# print(levels)
# for i,ll in enumerate(levels ):
#     print(f'i : {i}   level : {ll}')
# # print(adjust( ((3,1),(2,1)) , ((1,1),(1,1)) ,-1,0   ))


# print(adjust( ((1,2),(1,1)) , ((1,8),(1,8)) ,0,1   ))
# dx =[0,0,1,-1]
# dy = [1,-1,0,0]

# print(move(((1,1),(1,8)) ,  dx,dy))
# print(adj(((3,1),(1,3)),(red,blue)))