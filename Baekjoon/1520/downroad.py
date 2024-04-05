import sys
sys.setrecursionlimit(10**6)
N ,M  = list(map(int , input().split()))

height = []

for _ in range(N) :
    height.append(  list(  map(int,input().split())  )  )
    
    
x =[ [None for _ in range(M)] for _ in range(N)  ]

def indchk(i,j) :
    return i>= 0 and i< N and j>=0 and j<M
def dp (x , i,j) : 
    if x[i][j] is not None:
        return x[i][j]
    if i==0 and j==0 : 
        return 1
    ans = 0
    cur = height[i][j]
    if indchk(i,j-1) and height[i][j-1] > cur : ans += dp(x,i,j-1)
    if indchk(i-1,j) and height[i-1][j] > cur : ans +=dp(x,i-1,j)
    if indchk(i,j+1) and height[i][j+1] > cur: ans += dp(x,i,j+1)
    if indchk(i+1,j) and height[i+1][j] > cur : ans += dp(x,i+1,j)
    x[i][j] = ans
    return ans

print(dp(x,N-1,M-1))
# print(height)