def f(tmp , height,triangle):
    if height == len(triangle):
        return tmp
    k=[]
    k.append(tmp[0] + triangle[height][0])
    s=triangle[1:-1]
    for i in range(1,height) :

        k.append(max(tmp[i-1]+triangle[height][i] , tmp[i]+triangle[height][i]) )
    k.append(tmp[height-1]+triangle[height][height])
    return f(k,height+1,triangle)

def solution(triangle):
    answer = 0

    s=f([triangle[0][0]] , 1,triangle)
    answer=max(s)
    return answer