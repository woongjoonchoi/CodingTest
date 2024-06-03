
N = int(input())

orderli=[]
search_dict = {}
for _ in range(N*N) :
    a ,*b = map(int,input().split())
    
    b = set(b)
    di = (a,b)
    search_dict[a] =  b
    orderli.append(di)
    

def indchk(x,y):
    return x >=0 and x<N and y>=0 and y<N

deltax=[0,0,1,-1]
deltay=[1,-1,0,0]
di ={}
classroom = [[0 for _ in range(N)] for _ in range(N)]

score =0
score_dict= {0:0,1:1,2:10,3:100,4:1000}

for a in orderli :
    student , like = a
    ans = None
    max_like,max_emtpy   = 0, 0
    for i in range(N) :
        for j in range(N):
            pass
            like_count , empty_count = 0,0
            if classroom[i][j] >0 : continue
            
            
            
            for dx,dy in zip(deltax,deltay) :
                pass
                if not indchk(i+dx,j+dy) : continue
                if classroom[i+dx][j+dy] == 0 : empty_count +=1
                if classroom[i+dx][j+dy] in like : like_count+=1

            if ans is None : 
                max_like,max_emtpy = like_count,empty_count
                ans = (i,j)
                
                continue
        
          
            ### 1번인지 1번 갱신되면 갱신하고 continue
            

            if max_like < like_count : 
                max_like = like_count
                max_emtpy = empty_count
                ans= (i,j)
                
                continue
            elif max_like > like_count:
                continue
            

            ### 2번인지 2번 갱신되면 갱신하고 continue
            if max_emtpy < empty_count : 
                max_emtpy = empty_count
                ans = (i,j)
                
                continue
            elif max_emtpy > empty_count :
                continue
            ### 3번이닞 3번 갱신되면 갱신하고 continue
            

            if ans[0] > i  : 
                ans=(i,j)
                continue
            elif ans[0]  < i : 
                continue
            if ans[1] > j : 
                ans=(i,j)
                continue
            elif ans[1] <j : 
                continue
    classroom[ans[0]][ans[1]] = student

score = 0
for i in range(N) :
    for j in range(N) :
        like_count = 0
        like = search_dict[classroom[i][j]]
        for dx,dy in zip(deltax,deltay) :
            if not indchk(i+dx,j+dy) : continue
            if classroom[i+dx][j+dy] in like : like_count+=1
            

        score += score_dict[like_count]
        


print(score)            