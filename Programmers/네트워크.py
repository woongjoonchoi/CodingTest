cnt = 0 
def dfs(check,node,computers,n):
    global cnt
    if check[node] == 1:
        return
    for i in range(n):
        if i!=node and computers[node][i] == 1:
            check[i]=1
            cnt+=1
            return dfs(check,node,computers,n)
    return
def solution(n, computers):
    check=[0 for _ in range(n)]
    answer=0
    dfs=[]
    while 0 in check :
        dfs.append(check.index(0))
        check[check.index(0)] = 1
        while dfs :
            node = dfs.pop(0)
            check[node] = 1
            for i in range(n):
                if check[i] != 1 and computers[node][i] ==1 :
                    dfs.append(i)
                    check[i]=1
        print(dfs)
        answer+=1
    # answer = 0
    return answer