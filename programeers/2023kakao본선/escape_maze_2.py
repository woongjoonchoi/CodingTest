from collections import namedtuple

# def bfs(n,m,x,y,r,c,k)
# 52번째 줄 x,y = x+dx , y+dy 코드 빼먹음


# 실패함 시간초과 50,50,1500 되면 실패함
import time
def indchk(x,y,n,m) :
    return x>=1 and x<=n and y>=1 and y<=m
    
def solution(n, m, x, y, r, c, k):
    start = time.time()
    answer = 'impossible'
    temp_answer= ''
    remain = {'d' :0,'l':0,'r':0,'u':0}
    dp =  [ [ [None for _ in range(k+1)]  for _ in range(m+1) ]  for _ in range(n+1)]
    # vector = {(1,0):'d',(-1,0):'u' ,(0,1) :'r' ,(0,-1) :'l'}
    dp[x][y][0] = [0, {'d' :0,'l':0,'rl':0,'r' :0,'u':0}]
    # dp[x][y][0] =  {'d' :0,'l':0,'rl':0,'r' :0,'u':0}
    
    deltax= [1,0,0,-1]
    deltay = [0,-1,1,0]
    path = ['u','r','l','d']
    keys = ['d','l','rl','r' ,'u']
    ind = [1,2,3,4]

    for k in range(1,k+1) : 
        for i in range(1,n+1) :
            for j in range(1,m+1) :
                # new_path =[]
                new_string=None
                for dx,dy,p , v in zip(deltax,deltay,path,ind) :
                    if indchk(i+dx,j+dy,n,m) and dp[i+dx][j+dy][k-1] is not None :

                        temp_length = dp[i+dx][j+dy][k-1][0]
                        temp_di = dp[i+dx][j+dy][k-1][1]
                        # temp_di = dp[i+dx][j+dy][k-1]
                        # if len(temp_string) > 0 and temp_string[-1] =='r' and p =='l' :
                        if temp_length > 0 and temp_string[-1] =='r' and p =='l' :
                            temp_di['r']-=1
                            temp_di['rl'] +=1
                        else : 
                            temp_di[p] +=1
                        # temp_string.append(p)
                        if new_string is None :
                            # new_string= [temp_string,temp_di ]
                            new_string=[temp_length,temp_di]
                        # else : 
                        #     for key in keys :
                        #         if new_string[1][key] < temp_di[key] :
                        #             new_string[1] = temp_di
                        #             break
                        


                dp[i][j][k] = new_string
                    # print(new_path)
    # for k in keys : print(k)
    # if dp[r][c][k] is not None : answer = ''.join(dp[r][c][k][0])
    # print(['a'] +'b')
    # print("ab" >"ac")
    # print(dp[r][c][k])
    if answer is None : answer="impossible"
    print(f'time : {time.time()-start}')
    return answer