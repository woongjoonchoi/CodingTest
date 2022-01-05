di={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def jb(num,n):
    ans = ''
    while num>0:
        a = num%n
        num=num//n
        ans = di[a] + ans
    if ans == '':
        ans='0'
    return ans , len(ans)


def solution(n, t, m, p):
    answer = ''
    count = 0
    temp_ans=''
    # for i in range(100000):
    #     a=2
    num=0
    while count < t * m : 
        ans, temp = jb(num,n)
        num+=1
        count+=temp
        temp_ans+=ans

    for i in range(t):
        answer+=temp_ans[i*m+p-1]
    return answer


jb(0,10)