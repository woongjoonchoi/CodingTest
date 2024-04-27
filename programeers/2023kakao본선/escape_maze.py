from collections import namedtuple

# def bfs(n,m,x,y,r,c,k)

def indchk(x,y,n,m) :
    return x>=1 and x<=n and y>=1 and y<=m
    
def solution(n, m, x, y, r, c, k):
    # state = namedtuple('state' , ['pos','path'])
    answer = 'impossible'
    li = {'d' :0,'l':0,'r':0,'u':0}
    # start = state((x,y),'')
    start = (x,y)
    parent = {start:None}
    level=[start]
    deltax= [1,0,0,-1]
    deltay = [0,-1,1,0]
    path = ['d','l','r','u']
    # depth = 1
    while level :
        depth +=1
        new_explore = []
        for u in level :
            for dx,dy, p in zip(deltax,deltay,path) :
                if not indchk(u+dx,u+dy,n,m) : continue

                if (r,c) == (u+dx,u+dy) :
                    break
                parent[(u+dx,u+dy) ] = u
                new_explore.append((u+dx,u+dy))
                li[p] +=1
            else: 
                level = new_explore
            break
        else :
            continue
        break

    
    return answer