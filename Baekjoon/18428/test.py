import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(sys.stdin.readline())
# matrix =[]
T = []
O = []
count_O = 3
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# for i in range(n) :
#     matrix.append(sys.stdin.readline().rstrip().split())
matrix = [sys.stdin.readline().split() for __ in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 'T' :
            T.append((i,j))

for x,y in T :
    for i in range(4) :
        m = 1
        while x +m* dx[i] >= 0 and x +m* dx[i]   <n  and y+m* dy[i] >=0 \
            and y+m* dy[i] < n and matrix[x+m*dx[i]][y+dy[i] * m]  :
            matrix[x+m*dx[i]][y+m*dy[i]] = 'C'
            m+=1
        
            
            

a = [(1,2) , (3,4)]
# print(set(a))
for m in matrix :
    print(m)
print(matrix)