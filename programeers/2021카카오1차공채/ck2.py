def bitmask(order,di) :
    length = len(order)
    # di_s = {}
    for i in range(1<<length) :
        st = ''
        for k in range(length) :
            if 1<<k & i :
                st+=order[k]
        # print(len(st))
        if len(st) >= 2:
            di_s={}
            if len(st) not in di.keys():
                di[len(st)] = di_s
            if st not in di[len(st)].keys():
                di[len(st)][st] = 0
            di[len(st)][st]+=1
        print(di)
    return di
def solution(orders, course):
    answer = []
    di={}
    for i in orders:
        bitmask(i,di)
    # print(di)
    for l in course :
        # print(di.keys())
        
        if l in di.keys():
            # print(di[l])
            # print(di[l].items())
            s = sorted(di[l].items(),key=lambda x : x[1] ,reverse= True)
            mv=int(s[0][1])
            # print(s)
            # a= 2
            if mv >=2 :
                answer.append(s[0][0])
        # # mv=di[l][0][1]
        #         for k,v in di[l].items:
        #             if mv == v :
        #                 answer.append(k)
        #             else: 
        #                 break

    # print(answer)
    # for i in range(1000):
    #     for k in range(20):
    #         a = 1
    return answer

a = 'DA'
a=''.join(sorted(a))
print(a)
# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"] , [2,3,4])