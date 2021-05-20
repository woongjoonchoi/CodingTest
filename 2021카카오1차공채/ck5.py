count = [0 for _  in range(360001)]

nujuk = [0 for _ in range(360001)]
def t_s(t) :
    
    h,m,s = t.split(':')
    return int(h)*3600 + int(m)*60 + int(s)

def t_back(t) :
    h =  t//3600
    t = t % 3600
    m = t// 60
    t = t%60
    s = t
    h= '{0:02d}'.format(h)
    m= '{0:02d}'.format(m)
    s= '{0:02d}'.format(s)
    return h+":"+m+":" + s
def solution(play_time, adv_time, logs):
    global count
    global nujuk
    answer = ''
    ans = 0
    ind = 0
    p = t_s(play_time)
    a= t_s(adv_time)
    for l in logs :
        t1,t2 = l.split("-")
        t1 = t_s(t1)
        t2 = t_s(t2)
        count[t1] +=1
        count[t2] -=1
    for i in range(1, p) :
        count[i] +=count[i-1]

    for i in range(1,p) :
        count[i] +=count[i-1]
    for i in range(a-1, p):
        if i>=a :
            if count[i] - count[i-a] > ans :
                ans = max(ans,count[i] - count[i-a])
                ind = i-a + 1
        else :
            if count[i]> ans :
                ans = max(ans,count[i])
                ind = 0
    # ind = count.index(ans)-a +1
    answer = t_back(ind)
    return answer
solution(		"50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])