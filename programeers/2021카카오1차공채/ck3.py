def bin_search(score,arr) :
    start = 0
    
    end = len(arr)-1
    ans = len(arr)
    while start<=end :
        mid = int((start + end)/2)
        if arr[mid] >= score :
            ans = mid
            end = mid-1
        elif arr[mid] < score:
            start = mid + 1
    return len(arr) - ans 

def solution(info, query):
    answer = []
    lan=['java', 'cpp' , 'python']
    job = ['frontend' , 'backend']
    years = ['senior','junior']
    food = ['pizza','chicken']
    di = {}
    di['java'] = {}
    di['cpp'] = {}
    di['python'] = {}
    for k ,v in di.items():
        di[k]['backend'] = {}
        di[k]['frontend'] = {}
        for k2 ,v2 in di[k].items():
            di[k][k2]['junior'] = {}
            di[k][k2] ['senior'] = {}
            for k3,v3 in di[k][k2].items() :
                di[k][k2][k3]['pizza'] = {}
                di[k][k2][k3]['chicken'] = {}
                for k4,v4 in di[k][k2][k3].items() :
                    di[k][k2][k3][k4] = []
    for i in info:
        t = i.split(' ')
        # print(t)
        di[t[0]][t[1]][t[2]][t[3]].append(int(t[4]))
    for k ,v in di.items():
        for k2 ,v2 in di[k].items():
            for k3,v3 in di[k][k2].items() :
                for k4,v4 in di[k][k2][k3].items() :
                    di[k][k2][k3][k4].sort()
    for q in query:
        t= q.split(' and ')
        s = t.pop()
        s= s.split(' ')
        t= t+ s
        cd = []
        if t[0] == '-' :
            cd.append(lan)
        else :
            s = []
            s.append(t[0])
            cd.append(s)
        if t[1] == '-' :
            cd.append(job)
        else :
            s = []
            s.append(t[1])
            cd.append(s)        
        if t[2] == '-' :
            cd.append(years)
        else :
            s = []
            s.append(t[2])
            cd.append(s)    
        if t[3] == '-' :
            cd.append(food)
        else :
            s = []
            s.append(t[3])
            cd.append(s) 
        cd.append(int(t[4]))
        a= 0
        for k in cd[0] :
            for k2 in cd[1] :
                for k3 in cd[2] :
                    for k4 in cd[3] :
                        if di[k][k2][k3][k4] :
                            a += bin_search(cd[4] , di[k][k2][k3][k4])
        answer.append(a)
                        
# print(di)
    
    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    , ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])