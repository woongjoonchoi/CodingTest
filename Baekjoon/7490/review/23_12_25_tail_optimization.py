def calculate(n,operator,operand,result,expression):
    
    
    if n == N :
        if operand[0] == '+' :
            result = result + int(operand[1:])
        elif operand[0] == '-' :
            result = result - int(operand[1:])
        if result == 0 : print(expression)
        return
    
    for op in operator_list :
        _expression= expression+op+str(n+1)
        _result = result
        if op ==' ':
            calculate(n+1,op,operand+str(n+1),_result,_expression)
        elif operand[0] == '+' : 
            _result += int(operand[1:])
            calculate(n+1,op,op+str(n+1),_result,_expression)
        else :
            _result -= int(operand[1:])
            calculate(n+1,op,op+str(n+1),_result,_expression)
    
     


operator_list = [' ','+','-']


t = int(input())
Num = []
for i in range(t):
    Num.append(int(input()))
for i in range(t):
    N =Num[i]
    calculate(1,'+',"+1",0,"1")
    print()
    
    