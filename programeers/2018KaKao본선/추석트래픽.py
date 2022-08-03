import re
from datetime import datetime,timedelta
def starttime(line) :
    date, time , sec = line.split()
    h,m,s = time.split(':')
    end = 60 * 60 * int(h) + 60 * int(m) + float(s)
    start = end - float(sec[:-1]) + 0.001
    end=round(end,3)
    start=round(start,3)
    return start , end

def check(start,end,t_time) :
    cnt=0
    for k in t_time:
        # print("start: %f  end: %f" %(start,end) )
        # print("k[0] %f  k[1]  %f   %d "  %(k[0] , k[1] , k[0] - end))
        # print("%d  %d " %(start <= k[1] ,k[0] -end<=0  ) )
        if start <= k[1] and k[0] <= end :
            cnt+=1
    return cnt    
def solution(lines):
    t_time=[]
    for line in lines:
        start , end= starttime(line)
        t_time.append([start, end])
    max_cnt=0

    # print(t_time[0][0] >t_time[0][1])
    # print(check(t_time[0][0],t_time[0][1],t_time))
    for t in t_time :
        max_cnt=max(check(t[0],round(t[0]+0.999,3),t_time) , max_cnt)

        max_cnt=max(check(t[1],round(t[1]+0.999,3),t_time) , max_cnt)


    answer = max_cnt
    return answer
