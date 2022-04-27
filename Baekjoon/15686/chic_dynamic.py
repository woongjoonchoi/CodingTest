import sys

N,M = map(int,sys.stdin.readline().split())


# mat= []
    

home = []
chic = []

chic_dist = {}

for i in range(N) :
    temp = list(map(int,sys.stdin.readline().split()))
    
    for j in range(N):
        if temp[j] == 1:
            home.append((i,j))
            chic_dist[f'{i},{j}'] = 0
        elif temp[j] == 2 :
            chic.append((i,j))

# for i in range(N) :
#     for j in range(N) :
#         if mat[i][j] == 1 :
#             home.append((i,j))
#             chic_dist[f'{i},{j}'] = 0
            
#         elif mat[i][j] == 2 :
#             chic.append((i,j))


            

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
                
                if chic_dist[f'{h[0]},{h[1]}'] > (abs(h[0] - c[0])  + abs(c[1]-h[1])) :
                    temp_min += (abs(h[0] - c[0])  + abs(c[1]-h[1]))
                else :
                    temp_min +=  chic_dist[f'{h[0]},{h[1]}']
            if not flag :
                first_chic = (c[0] , c[1])
                flag = True
            if temp_min < city_chic:
                city_chic = temp_min 
                first_chic = (c[0] , c[1])
        for h in home :
            if chic_dist[f'{h[0]},{h[1]}'] > (abs(h[0] - first_chic[0])  + abs(first_chic[1]-h[1])) :
                chic_dist[f'{h[0]},{h[1]}'] = (abs(h[0] - first_chic[0])  + abs(first_chic[1]-h[1]))
        
print(city_chic)

                    
        
                    
                
            