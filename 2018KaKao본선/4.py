def t_m(hm):
    h,m = hm.split(':')
    return int(h) * 60 + int(m) 

def m_t(mm):
    h=mm//60
    m=mm%60
    h="{0:02d}".format(h)
    m="{0:02d}".format(m)
    return h+":"+m
def solution(n, t, m, timetable):
    
    answer = ''
    arr = 540
    temp=0
    tt_cp={}
    count=1
    bus_ind=0
    # remain=n*m
    remain=m
    for hm in timetable:
        k = t_m(hm)
        if k not in tt_cp.keys():
            tt_cp[k]=0
        tt_cp[k]+=1
    tt_cp = sorted(tt_cp.items())
    t_cp=[]
    for k in tt_cp :
        t_cp.append(list(k))
    tt_cp=t_cp
    for i in range(n):
        arr=540+i*t
        temp_m = m
        # bus_ind=i
        while tt_cp and  tt_cp[0][0] <=arr and temp_m>0:
            # bus_ind=i
            temp = tt_cp[0][0]
            if temp_m >= tt_cp[0][1]:
                 temp_m-=tt_cp[0][1]
                 tt_cp.pop(0)
            else:
                tt_cp[0][1]-=temp_m
                temp_m=0
        if i == n-1 :
            remain=temp_m

    if remain<1:
        temp-=1
    else:
        temp = 540 + t *(n-1)

    # else:

    # temp-=1
    # if temp
    answer = m_t(temp)
    return answer

# solution(	2, 10, 2, ["09:10", "09:09", "08:00"])
solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
# solution(1, 1, 1, ["23:59"])