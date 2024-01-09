def tovalue(exp) :
    i = 0
    result = 0
    operand = 0
    past_op = '+'
    while i < len(exp) :
        if exp[i] == '+' or exp[i] == '-'  :
            
            if past_op == '+' :
                result += operand
            else :
                result -= operand
            operand = 0
            past_op = exp[i]
        elif exp[i] ==' ':
            pass
        else :
            operand = operand * 10 + int(exp[i])
        i+=1
    if past_op == '+' :
        result += operand
    else :
        result -= operand
    return result
            
def calculate(num, exp) :
    if num == n :
        
        if tovalue(exp) == 0 :
            print(exp)
        return 
    
    for opr in op:
        calculate(num+1,exp+opr+str(num+1))
    
    
    

op= [' ','+','-']

test_case = int(input())
n_list = []
for _ in range(test_case) :
    n_list.append(int(input()))

for n in n_list :
    calculate(1,"1")
    print()
    