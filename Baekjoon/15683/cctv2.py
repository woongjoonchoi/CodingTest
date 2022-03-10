import sys
import copy
N , M = list(map(int,sys.stdin.readline().split()))

office = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

min_val = N * M 
rotate = { 'i' : [0,1] ,'j' :  [-1,0]}

cc1 = [[1,0]]

cc2 = [[0,1],[0,-1]]

cc3 = [[0,1] ,[-1,0]]

cc4 = [[0,1],[0,-1],[-1,0]]

cc5 = [[0,1],[0,-1],[1,0],[-1,0]]

rotate_dir=[cc1,cc2,cc3,cc4,cc5]

rotate_count = [4,2,4,4,1]


# depth =0
temp_count = 0
rotate_state=[]
wall = 0
# check
walled= set()
for x in range(N) : 
    for y in range(M) :
        if office[x][y] != 0 and office[x][y] !=6 : 
            di={}
            di['pos'] = (x,y)
            di['rotate_num'] = office[x][y]
            rotate_state.append(di)
        elif office[x][y] == 6 :
            walled.add((x,y))
            wall +=1
   
def vecmul(r,scalar) :
    return [ k * scalar for k in r]

def vecadd(r,s) :
    return [a1+a2 for a1,a2 in zip(r,s)]

# check end
def detect(ind) :
    # global depth
    global temp_count
    global marked
    global min_val
    global N 
    global M
    global wall
    # depth = ind
    
    
    # if min_val <=N*M -temp_count - wall:
    #     return 
    if ind == len(rotate_state) :
        # print(min_val)
        # for k in office :
        #     print(k)
        # print('-------------------')
        # if min_val <=N*M -temp_count - wall:
        #     # return 
        min_val = min(N*M -len(marked)-wall ,min_val)
        for k in rotate_state :
            assert k['pos'] in marked 
        for k in walled :
            assert k not in marked , f"walled  {k}"
        temp = office[:]

        assert temp is not office
        
        
        # print('-------------------')
        # print(marked)
        # print(min_val)
        # print(f'temp count :{temp_count}')
        # for  i  ,kk in enumerate(temp) :
        #     for  j, jj in enumerate(kk) :
        #         if (i,j) in marked and jj == 0:
        #             temp[i][j] = '#'
        #     print(' '.join(list(map(str,temp[i]))))
        return 

    (x,y) , cctv_num = rotate_state[ind]['pos'] , rotate_state[ind]['rotate_num']-1
    count = rotate_count[cctv_num]
    # dx , dy = rotate_dir[cctv_num]
    
    # 3 . rotate shared , new object need
    temp_rotate = copy.deepcopy(rotate_dir[cctv_num][:][:])
    # assert temp_rotate 
    for i in range(count) : 
        temp_set=set()
        
        for dd in range(len(rotate_dir[cctv_num])) :
            # dx,dy = rotate_dir[cctv_num][dd]
            assert temp_rotate[dd] is not rotate_dir[cctv_num][dd]
            dx,dy = temp_rotate[dd]
            
            # camera exclude
            
            # 2.set operation vs method , type differ
            # marked.update((x,y))
            if (x,y) not in marked :
                marked.add((x,y))
                # temp_set.update((x,y))
                temp_set.add((x,y))
            temp_x ,temp_y = x+dx,y+dy
            while 0<=temp_x<N and 0<=temp_y<M and office[temp_x][temp_y] != 6 :
                # marked.update((temp_x,temp_y))
                # temp_set.update((temp_x,temp_y))
                for k in walled :
                    assert k != (temp_x , temp_y) , f"walled {temp_x ,temp_y} == {k}  camera {x,y}  wall {walled}"
                
                
                # 4 . 중복해서 셋음
                if (temp_x,temp_y) not in marked :
                    temp_set.add((temp_x,temp_y))
                marked.add((temp_x,temp_y))
                
                temp_x+=dx
                temp_y+=dy
            # rotate_dir[cctv_num][dd] = vecadd(vecmul(rotate['i'] , dx) , vecmul(rotate['j'] , dy ))
            temp_rotate[dd] = vecadd(vecmul(rotate['i'] , dx) , vecmul(rotate['j'] , dy ))
        temp_count += len(temp_set)
        assert temp_count == len(marked) , f"wrong temp_count {temp_count}   marked {len(marked)}"
        detect(ind+1)
        temp_count -= len(temp_set)
        marked -= temp_set
        

marked = set({})


detect(0)

print(min_val)
# test =[[1,0] , [0,1],[-1,0],[0,-1]]
# for i in range(4) :
#     for dd in range(len(rotate_dir[0])) :
#         dx,dy = rotate_dir[0][dd]
#         assert test[i] == rotate_dir[0][dd] , f"{test[i]}  {rotate_dir[0][dd]}"
#         rotate_dir[0][dd] = vecadd(vecmul(rotate['i'] , dx) , vecmul(rotate['j'] , dy ))
# print(rotate)
# print(rotate_state)
    


# kkk = set()
# temp = set()

# kkk.update((1,2))
# temp.update((1,2))

# print(kkk)
# print(temp)

# print(kkk-temp)


# print()