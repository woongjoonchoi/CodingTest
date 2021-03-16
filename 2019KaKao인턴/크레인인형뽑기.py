def reverse(board) :
    temp=[]
    for i in range(0,len(board)) :
        temp.append([])
    for x in board :
        for i in range(0,len(x)):
            if(x[i]>0) : 
                temp[i].insert(0,x[i])
    
    return temp
            

def solution(board, moves):
    answer = 0
    temp = reverse(board)
    basket=[]
    
    # for c in temp :
    #     print(c)
    # print(temp[1])
    for m in moves:
        if len(temp[m-1]) >0 :
            d = temp[m-1].pop()
            if  len(basket) > 0 and d == basket[-1] : 
                basket.pop()
                answer+=2
                continue
            else:
                basket.append(d)
        
    # answer=len(basket)
        
    return answer