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
            

for k in combinations(chick,M) :
    # print(k)
    city_chic_temp = 0
    for h in home :
        chic_dist = N**3
        
        for c in k :
            chic_dist = min(chic_dist , abs(c[0]-h[0]) + abs(c[1] - h[1]))
        city_chic_temp += chic_dist 
        if city_chic >0 and city_chic_temp >= city_chic :
            break
    
            
    if city_chic < 0 : 
        city_chic = city_chic_temp
        continue
    city_chic = min(city_chic_temp, city_chic)
    
    a= 4
    
    
    
print(city_chic)


