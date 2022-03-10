import sys
from operator import mul
N ,M  = list(map(int,sys.stdin.readline().split()))

office = [ list(map(int,sys.stdin.readline().split())) for i in range(N)]
next_state = []
cctv_loc = []
for x in range(len(office)) :
    for y in range(len(office)) :
        if office[x][y] !=0 :
            cctv_loc.append([x,y])
            if office[x][y] == 1:
                next_state.append(cc1)
                # cctv_loc.append([x,y])
            elif office[x][y] == 2:
                next_state.append(cc2)
                cctv_loc.append
            elif office[x][y] == 3:
                next_state.append(cc3)
            elif office[x][y] == 4:
                next_state.append(cc4)
            elif office[x][y] == 5:
                next_state.append(cc5)

i=0
def cc1() :
    deltax = [0,0,1,-1]
    deltay= [ 1,-1,0,0]
    direction = [1,0]
    for dx,dy in zip(deltax,deltay) :
        # t_x = list(map(mul,direction[0] 
        # dx ,dy = [sum(x) for x in direction]
        x+=dx
        y+=dy
        while 0<=x<N and 0<=y<M and  office[x][y] != 6 :
            office[x][y] = -1
            x+=dx
            y+=dy
        # next_state[i]
            
    ...
def cc2():
    
    x,y = 0,0
    
    # x1 ,y1= x, y
    deltax =[1,0]
    deltay =[0,1]
    
    for dx ,dy in zip(deltax,deltay) :
        x1 ,y1= x, y
        x2 ,y2  = x, y
        x1+=dx
        y1+=dy
        while 0<=x1<N and 0<=y1<M and office[x1][y1] != 6 :
            office[x1][y1] = -1
            x1+=dx
            y1+=dy
        x2-=dx
        y2-=dy
        while 0<=x1<N and 0<=y1<M and office[x2][y2] != 6 :
            office[x2][y2] = -1
            x2-=dx
            y2-=dy
        next_state[i]
    ...
    
def cc3(next_state=None) :
    
    x,y = 0 , 0
    deltax=[-1,-1,1,1]
    deltay=[1,-1,-1,1]
    
    for dx,dy in zip(deltax,deltay) :
        x1,y1,x2,y2 = x,y,x,y
        x1+=dx
        y1+=dy
        while 0<=x1<N and 0<=y1<M and office[x1][y1] != 6:
            office[x1][y1] = -1
            x1+=dx
            y1+=dy
        
    ...
    
def cc4(next_state = None) :
    x,y = 0,0
    deltax = [-1,0,1,0]
    deltay = [0,-1,0,1]
    for dx,dy in zip(deltax,deltay) :
        x1,x2,x2,y2,x3,y3 = x,y , x,y,x,y
        while 0<=x1<N and 0<=y1<M and office[x1][y1] != 6:
            office[x1][y1] = -1
            x1+=dx
            y1+=dy        
        if dx!=0 :
            dx = 0
            dy = 1
        else :
            dx = 1
            dy = 0
        x2+=dx
        y2+=dy
        while 0<=x2<N and 0<=y2<M and office[x2][y2] != 6 :
            office[x2][y2] = -1
            x2+=dx
            y2+=dy
        x3-=dx
        y3-=dy
        while 0<=x3<N and 0<=y3<M and office[x3][y3] != 6 :
            office[x3][y3] = -1
            x3-=dx
            y3-=dy
        
   
    ...
def cc5(next_state = None):
    x,y= 0,0
    
    
    x1,x2,x3,x4,y1,y2,y3,y4 = x,x,x,x,y,y,y,y
    
    dx ,dy= 1 ,0
    x2+=dx
    y2+=dy
    while 0<=x2<N and 0<=y2<M and office[x2][y2] != 6 :
        office[x2][y2] = -1
        x2+=dx
        y2+=dy
    x3-=dx
    y3-=dy
    while 0<=x3<N and 0<=y3<M and office[x3][y3] != 6 :
        office[x3][y3] = -1
        x3-=dx
        y3-=dy
    dx ,dy = 0,1 
    x3+=dx
    y3+=dy
    while 0<=x3<N and 0<=y3<M and office[x3][y3] != 6 :
        office[x3][y3] = -1
        x3+=dx
        y3+=dy
    x4-=dx
    y4-=dy
    while 0<=x4<N and 0<=y3<M and office[x4][y3] != 6 :
        office[x4][y3] = -1
        x4-=dx
        y4-=dy
    
    ...

print(office)