from collections import namedtuple

# def bfs(n,m,x,y,r,c,k)
# 52번째 줄 x,y = x+dx , y+dy 코드 빼먹음
def indchk(x,y,n,m) :
    return x>=1 and x<=n and y>=1 and y<=m
    
def solution(n, m, x, y, r, c, k):
    
    answer = 'impossible'
    
    deltax = [1,0,0,-1]
    deltay = [0,-1,1,0]  
    direction=['d','l','r','u']
    dp=[[[False for _ in range(k+1)]  for _ in range(m+1)] for _ in range(n+1)]
    
    dp[r][c][0]= True
    
    for d in range(1,k+1):
        for i in range(1,n+1):
            for j in range(1,m+1):
                for dx,dy in zip(deltax,deltay) :
                    if not indchk(i+dx,j+dy,n,m) : continue
                    if dp[i+dx][j+dy][d-1] : 
                        dp[i][j][d] = True
                        break 
                    
    # print(dp[x][y][k])
    if not dp[x][y][k] : return answer
    
    answer, cur_x ,cur_y ="", x,y
    for d in range(k,0,-1):
        
        for dx,dy,dr in zip(deltax,deltay,direction):
            if not indchk(cur_x+dx,cur_y+dy,n,m) : continue
            if dp[cur_x+dx][cur_y+dy][d-1] : 
                answer += dr
                cur_x,cur_y = cur_x+dx , cur_y+dy
                break
                
            
    
        # print(d)
        
                    
                
                
    return answer