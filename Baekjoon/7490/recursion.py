import sys

l  = int(input())


num = [int(input()) for _ in range(l)]

def eval(left , right,i , before , s) :
    if i == len(s) :
        if before =='+' :
            return left + int(right)
        else  :
            return left - int(right)
    if s[i] == ' ':
        pass 
    elif s[i] == '+' or s[i] == '-' :
        if before =='+' :
            left += int(right)
        else :
            left -= int(right)
        right=''
        before=s[i]
    else : 
        right +=s[i]
    return eval(left,right,i+1,before,s)

def make_exp(i,n , s ) :
    if i == n :
        # s += str(i)
        if eval(0,'' , 0 , '+' , s + str(i)) ==0 :
            print(s+ str(i))
        return 
    k = [' ','+' ,'-']
    for ss in k : 
        make_exp(i+1 , n , s + str(i) + ss )
            
# make_exp(1,7,'')

for n in num :
    make_exp(1,n,'')
    print('')