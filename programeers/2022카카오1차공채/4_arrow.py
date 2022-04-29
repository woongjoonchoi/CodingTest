max_score = 0
max_arrow = []

def recursive(n , info , result , score,arrow ) :
    global max_score
    global max_arrow
            
    if n>0 and score <0 :
        if max_score  < result : 
            max_score = result 
            max_arrow = []
            arrow[-1] += n
            max_arrow.append(arrow)
        elif max_score == result :
            arrow[-1] += n
            max_arrow.append(arrow)
        return
    if n == 0 :
        
        for i in range(score+1) :
            if info[10-i] >0 :
                result -= i
        # return
        if max_score <result :
            
            max_score = result 
            print(f'max_score : {max_score}')
            max_arrow = []
            max_arrow.append(arrow+[0] * (score+1))
            print(f'max_arrow : {max_arrow}')
        elif max_score == result :
            # pass
            max_arrow.append(arrow+[0] * (score+1) )
        return
            
    for i in range(2) :
        temp = n
        if i == 0 :
            temp-=(info[10-score]+1)
            if temp < 0: 
                temp = n
                result-=score
            else :
                result += score
        else :
            if info[10-score] > 0 :
                result-=score

        recursive(temp,info,result,score-1 , arrow + [n-temp])
        result -= score
    
    
def solution(n, info):
    answer = []
    # temp = []
    
    recursive(   n ,info,0,10 , [])
    print(max_score)
    print(max_arrow)
    if len(max_arrow ) == 0 :
        answer = [-1]
    else :
        answer= sorted(max_arrow)[0]
    return answer

# solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])

# solution(	9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])

# solution(	10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])

solution(11, [0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 1])
arr = [  [1,2,0,6,4]  , [1,0,0,0,2] ,[1,4,5,6,8] , [1,4,7,6,8]]

print(sorted(arr ,reverse= True) )
# print(list(reversed([1,2,3,4])))
# print(arr)
# print( map())

# 1 . base case 설정

# 2. recursion 이후 state 복원

# 3 . python list sort에 대한 이해 

# print(sorted(list(map(lambda x : x.reverse() , arr)), reverse = True) )