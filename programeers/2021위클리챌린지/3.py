from collections import deque
from collections import defaultdict
import copy
dx = [1,-1, 0,0]
dy = [0,0,1,-1]

def rotate(x,y,i):
    if i==0 :
        return [-x,-y]
    elif i==1:
        return [y,-x]
    elif i==2 :
        return [-y,x]
def rotate_b(x,y,n) :
    return [y,n-1-x]
def all_b(ans) :
    new_ans = []
    new_ans.append(ans) 
    for i in range(3):
        temp = []
        for j in range(len(ans)) :
            temp.append(rotate(ans[j][0],ans[j][1],i))
        temp = go_zero(temp)
        new_ans.append(temp)
    return new_ans
def go_zero(ans) :
    min_x = 100
    min_y = 100
    ans=copy.copy(ans)
    for x,y in ans :
        min_x = min(min_x , x)
        min_y = min(min_y , y)
    for i in range(len(ans)) :
        ans[i][0] -= min_x
        ans[i][1] -= min_y
    return ans
def check(x,y, n) :
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True
def bfs(matrix ,x , y,color) :
    n = len(matrix)
    dist = [ [0 for _ in range(n)] for _ in range(n)]
    q= deque()
    q.append((x,y))
    ans = []
    while q :
        s_x,s_y = q.popleft()
        dist[s_x][s_y] = 1
        for i in range(4):
            n_x = s_x + dx[i]
            n_y = s_y + dy[i]
            if check(n_x, n_y , n ) and matrix[n_x][n_y] ==color and dist[n_x][n_y] == 0 :
                dist[n_x][n_y] = 1
                q.append((n_x,n_y))
        dist[s_x][s_y] = 2
        ans.append([s_x, s_y])
    return ans
def idd(s,g_z) :
    g_z.sort()
    for i in range(len(s)) :
        s[i].sort()
        
    for i in range(len(s)) :
        flag = True
        for j in range(len(s[i])):
            
            for k in range(2):
                if s[i][j][k] != g_z[j][k]: 
                    flag=False
                    break
        if flag == True:
            return True
    return False
             
def solution(game_board, table):
    answer = 0
    t = len(table)
    g = len(game_board)
    all_t = {}
    check_t={}
    for i in range(t) :
        for j in range(t) :
            if table[i][j] == 1 :
                s_z = bfs(table, i, j,1)
                for b1 ,b2 in s_z :
                    table[b1][b2] = 0
                s_z = go_zero(s_z)
                if len(s_z) not in all_t.keys():
                    all_t[len(s_z)] =[]
                    check_t[len(s_z)] =[]
                all_t[len(s_z)].append(all_b(s_z))
                check_t[len(s_z)].append(0)
    for i in range(g) :
        for j in range(g) :
            if game_board[i][j] == 0 :
                o_g = bfs(game_board, i, j,0)      
                g_z = go_zero(copy.deepcopy(o_g))
                len_gb = len(g_z)
                if len_gb in all_t.keys():
                    for ind,s in enumerate(all_t[len_gb]) :
                        if check_t[len_gb][ind] == 1 : continue
                        if idd(s,g_z) == True :
                            check_t[len_gb][ind] = 1
                            answer+=len_gb
                            for g1,g2 in o_g:
                                game_board[g1][g2] = 1
                            break
    return answer