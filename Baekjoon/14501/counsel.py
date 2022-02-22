import sys

n  = int(sys.stdin.readline())
P = []
T  =[]
for i in range(n) :
    t , p = list(map(int,sys.stdin.readline().split()) )
    T.append(t)
    P.append(p)

# n=5
    
f = [0 for _ in range(n+1)]
for i in range(n-1,-1,-1) :
    # print(i)
    start = i
    consum = T[i]
    money = 0
    if start + consum<= n :
        money += P[i]
        money += f[start +consum]
            
    f[i] = max(money,f[i+1])

    
# p[rint(f)]
print(max(f))
# print(f)    
    