def calculate(n,exp) :
    
    if n == N :
        sum = 0
        operand= "+"
        for e in exp :
            asi = ord(e)-ord('0')
            if asi >=1 and asi<=9 :
                operand +=e
            elif e == ' ':
                pass
            elif operand[0] =='+' :
                sum += int(operand[1:])
                operand = e
            else  :
                sum -= int(operand[1:])
                operand = e             
        _asi =  ord(operand[0])-ord('0')
        if (_asi >=1 and _asi<=9) or (operand[0] == '+')  :
            sum += int(operand[1:])
        else : 
            sum-= int(operand[1:])
        if sum == 0:
            print(exp)
        return 
        
    for op in operator_list :
        calculate(n+1,exp+op+str(n+1))
    
        
    
    

operator_list = [' ','+' , '-']

t = int(input())
Num =[]
for  _ in range(t) :
    Num.append(int(input()))
    
for i in range(t) :
    N = Num[i]
    calculate(1,"1")
    print()
# print(ord('3')-ord('0'))