
import operator
op = [' ','+' ,'-']
calcul = {'+':operator.add, '-' :operator.sub}
base_num = -1
def expression_cal(num,left,right,expression,past_op) :
    
    if num == base_num +1 :
        left = calcul[past_op](left,right)
        # print(f'left :{left} expression :{expression}')
        if left == 0 :
            print(expression)
        return 
    
    for opr in op :
        new_left ,new_right = left,right 
        new_past_op = past_op
        if opr == ' ':
            new_right = new_right*10 +num
        else :
            # print(f"new_past_op : {new_past_op}")
            new_left = calcul[new_past_op](new_left,new_right)
            new_right = num
            new_past_op = opr
            
        expression_cal(num+1,new_left,new_right,expression+opr+str(num) ,new_past_op )
        
    # pass

n = int(input())
num_list = []
for i in range(n) :
    num_list.append(int(input()))
for i in range(n) :
    # global base_num
    num = num_list[i]
    base_num = num
    expression_cal(2,0,1,"1","+")
    print()
    
# c= operator.add(1,2)

# print(c)
    