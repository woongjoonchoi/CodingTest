case=int(input())
N = []
for i in range(case):
    n = int(input())
    N.append(n)
    
oper = (' ' , '+' ,'-')


def make_zero(num , steps ,  left_opr,right_opr   , op , exper ) :
    if steps == num   : 
        prev_left = left_opr
        if op == '+' : left_opr += right_opr
        elif op == '-' : left_opr -= right_opr
        if left_opr == 0 : 
            # print("left {} right {}  op {}".format(prev_left,right_opr,op))
            print(exper[2:])
        return 
    for _op in oper :
        if _op == ' ' : make_zero(num,steps+1,left_opr ,right_opr *10 +steps+ 1 ,op , exper + _op + str(steps+1))
        else :
            _left_opr = 0 
            if op == '+' : _left_opr = left_opr+right_opr
            elif op == '-' :  _left_opr = left_opr - right_opr
            make_zero(num,steps+1,_left_opr, steps+1 , _op,exper+ _op + str(steps+1))


for _num in N :
    make_zero(_num,1, 0,1,'+',"0+1")
    print()
    
    
    
#1  .첫번째 오류
# def mak_zero base case 부분
# steps == num+ 1 이라고함

# 이떄 , steps 4 , op : + , left_opr :-4 , right_opr :4 , exper : +1-2-3
# 여기서 left_opr + right_opr = 0 -> exper[1:] = 1-2-3


#2. 두번째 오류


# exper+op+str(right_opr)  
# -> right_opr 값이 세자리 네자리고 갈수 있기 때문에  1+2-3 4 45 456 4567 이런식으로 찍힘
# 
# exper+op+str(steps)

#위와같이 수정