


op = [' ' , '+','-']

t = int(input())

n_list = []

for _ in range(t):
    n_list.append(int(input()))
    
def calculate(num,result,operand,post_op,exp) :
    
    if num == n :
        # print(f"exp : {exp}  ,operand : {operand}, post_op: {post_op} result : {result}")
        if post_op == '+' :
            result += operand
        elif post_op == '-' :
            result -= operand
        if result == 0 :
            print(exp)
        # print(f"exp : {exp}  , result : {result}")
        
        return
    
    for opr in op : 
        next_num = num+1
        temp_operand=operand
        temp_result = result
        temp_op = post_op
        if opr == ' ' :
            temp_operand = operand * 10 + next_num
            
        else :
            if post_op == '+' :
                temp_result += operand
            else :
                temp_result -= operand
            temp_operand = next_num
            temp_op = opr
        calculate(next_num,temp_result,temp_operand,temp_op,exp + opr + str(next_num))
        
        
for n in n_list:
    calculate(1,0,1,'+',"1")
    print()
        
            