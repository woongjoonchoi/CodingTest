from collections import namedtuple

# def bfs(n,m,x,y,r,c,k)
# 52번째 줄 x,y = x+dx , y+dy 코드 빼먹음
def indchk(x,y,n,m) :
    return x>=1 and x<=n and y>=1 and y<=m
    
def solution(n, m, x, y, r, c, k):
    
    answer = 'impossible'
    temp_answer= ''
    remain = {'d' :0,'l':0,'r':0,'u':0}
    # vector = {(1,0):'d',(-1,0):'u' ,(0,1) :'r' ,(0,-1) :'l'}
    start = (x,y)
    x_diff ,y_diff= x-r,  y-c
    if x_diff>0 :
        remain['u'] += x_diff 
    else :
        remain['d'] += -1 * x_diff
    if y_diff >0 :
        remain['l'] += y_diff
    else :
        remain['r'] += -1 * y_diff
    
    print(remain)
        
    
    deltax= [1,0,0,-1]
    deltay = [0,-1,1,0]
    path = ['d','l','r','u']
    rev = {'d' : 'u','l' : 'r','r' : 'l','u' : 'd'}
    
    remain_num = abs(x_diff) + abs(y_diff)
    process = 0
    while remain_num + process < k:
        for dx,dy,p in zip(deltax,deltay,path) :
            if not indchk(x+dx,y+dy,n,m) : continue
            if remain[p] >0 :
                temp_answer +=p
                remain[p]-=1
                remain_num-=1
                process +=1
                x ,y = x+dx,y+dy
                break
            else :
                # temp_answer += c
                # process +=2
                remain[rev[p]] +=1
                temp_answer += p
                process +=1
                remain_num +=1
                x ,y = x+dx,y+dy
                break
        
        # print(f'temp_answer  :{temp_answer}')
        # print(f'process :{process}')
        # print(f'remain_num : {remain_num}')
        # print(f'remain :{remain}')
        # print(f'x ,y :{x}  {y}')
        # print('----------------------')
    # print(f'temp_answer  :{temp_answer}')
    # print(f'process :{process}')
    # print(f'remain_num : {remain_num}')
    # print(f'remain :{remain}')
    # print(f'x ,y :{x}  {y}')
    if remain_num + process ==k :
        for  p in path :
            temp_answer += p * remain[p]
        answer= temp_answer
    # elif remain_num + process > k :
    #     answer
        
    print(f'temp_answer  :{temp_answer}')
    # print(f'process :{process}')
    # print(f'remain_num : {remain_num}')
                
                
    return answer