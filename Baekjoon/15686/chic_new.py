import sys
from itertools import combinations

N,M = map(int,sys.stdin.readline().split())

mat = []

for i in range(N) :
    mat.append(list(map(int,sys.stdin.readline().split())))

home = []

chick = []


# def cal_min()
city_chic = -1

for i in range(N) :
    for j in range(N) :
        if mat[i][j] == 1 :
            home.append((i,j))
            
        elif mat[i][j] == 2 :
            chick.append((i,j))
            
chic_dist = []

for h in home :
    dist= []
    for c in chick :
        dist.append(abs(h[0] -c[0] )  + abs(h[1] - c[1]))
    chic_dist.append(dist)

# chic_dist = [list(map(  lambda c : abs(h[0] -c[0] )  + abs(h[1] - c[1])  , chick )  ) for h in home ]

chic_dist = [list(map(  lambda h : abs(h[0] -c[0] )  + abs(h[1] - c[1])  , home )  ) for c in chick ]

index = [i  for i in range(len(chick))]

for k in combinations(index,M) :
    # print(k)
    city_chic_temp = 0 
    
    # for i in range(len(chic_dist)) :
    #     temp_val  = 0
    #     for j in k :
    #         if temp_val ==0 :
    #             temp_val = chic_dist[i][j]
    #         else :
    #             temp_val = min(chic_dist[i][j] , temp_val)
    #     city_chic_temp += temp_val
    # for cc in [chic_dist[i] for i in k] :
        
    
    
    # temp_chic  = map(min , zip(*[chic_dist[i] for i in k]))
    
    for ccc in zip(*[chic_dist[i] for i in k]) :
        city_chic_temp += min(ccc)
    
    # sum_city_chic = 0
    # for k in temp_chic :
    #     city_chic_temp += k
    
    
    # city_chic_temp  = sum(map(min , [chic_dist[i] for i in k] ) ) 
    
    if city_chic == - 1 :
        city_chic  = city_chic_temp
    else :
        city_chic = min(city_chic_temp, city_chic)

    
    
print(city_chic)


