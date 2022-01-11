import itertools
import sys
n = int(sys.stdin.readline())
# print(n)
matrix =[]
S = []
T = []
O = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n) :
    matrix.append(sys.stdin.readline().rstrip().split())
    
    
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 'T' :
            T.append((i,j))


for x,y in T :
    for i in range(4) :
        if x + dx[i] >= 0 and x +dx[i] < n and y + dy[i] >=0 and y+dy[i] < n :
            pass
        for m in range()