import sys
from itertools import combinations

import random




# N,M = map(int,sys.stdin.readline().split())
N = random.randint(2,7)
M = random.randint(1,4)

home_num = random.randint(1,2*N+1)
chic_num = random.randint(M,14)
print(f'N : {N} , M : {M} , home_num : {home_num} , chic_num : {chic_num}')

N_rand = [i for i in range(0,N*N)]

position = random.sample(N_rand,chic_num+home_num)

print(position)
# print(len(position))
# exit()
# random.sample(N_rand,)
mat = [['0' for _ in range(N)] for _ in range(N)]
print(f'{N} {M}')


home = []
chic = []

chic_dist = {}

for  i,p in enumerate(position) :
    if i < home_num :
        home.append((p//N,p%N))
        mat[p//N][p%N] = '1'
        chic_dist[f'{p//N},{p%N}'] = 0
    else :
        chic.append((p//N,p%N))
        mat[p//N][p%N] = '2'
        
for k in range(N) :
    stin = ' '.join(mat[k])
    print(stin)
    # print(mat[i])

# exit()


city_chic = -1

first_chic = None

m_candi = set()
for i in range(M) :
    
    if i == 0 :
        for c in chic :
            chic_dist_temp=0
            for h in home :
                chic_dist_temp+=(abs(h[0] - c[0])  + abs(c[1]-h[1]))
            if city_chic< 0 :
                city_chic = chic_dist_temp 
                first_chic = (c[0] , c[1])
            elif chic_dist_temp < city_chic  :
                city_chic = chic_dist_temp 
                first_chic = (c[0] , c[1])
        for h in home :
            chic_dist[f'{h[0]},{h[1]}'] = (abs(h[0] - first_chic[0])  + abs(first_chic[1]-h[1]))
        m_candi.add(first_chic)
    else :
        
        flag = False
        for i ,c in enumerate(chic) :
            
            # 정답에 넣엇던 후보자 제외
            if c in m_candi :
                continue
            temp_min = 0
            for h in home:
                
                min_dist = min( chic_dist[f'{h[0]},{h[1]}'] , (abs(h[0] - c[0])  + abs(c[1]-h[1])))
                temp_min +=min_dist
            if not flag :
                first_chic = (c[0] , c[1])
                flag = True
            if temp_min < city_chic:
                city_chic = temp_min 
                first_chic = (c[0] , c[1])
        for h in home :
            if chic_dist[f'{h[0]},{h[1]}'] > (abs(h[0] - first_chic[0])  + abs(first_chic[1]-h[1])) :
                chic_dist[f'{h[0]},{h[1]}'] = (abs(h[0] - first_chic[0])  + abs(first_chic[1]-h[1]))
                

# assert city_chic > 0  , city_chic
        
city_chic_second = -1

for k in combinations(chic,M) :
    # print(k)
    city_chic_temp = 0
    for h in home :
        chic_dist = N**3
        
        for c in k :
            chic_dist = min(chic_dist , abs(c[0]-h[0]) + abs(c[1] - h[1]))
        city_chic_temp += chic_dist 
        if city_chic_second >0 and city_chic_temp >= city_chic_second :
            break
    
            
    if city_chic_second < 0 : 
        city_chic_second = city_chic_temp
        continue
    city_chic_second = min(city_chic_temp, city_chic_second)
    
        
# assert abs(city_chic - city_chic_second) == 12 , "eror"

# assert N >25 , "error"
print(city_chic)
print(city_chic_second)
                    
        
                    
                
            