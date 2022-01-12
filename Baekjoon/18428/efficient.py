import itertools
import sys
import pprint
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
        else : 
            continue
        if dx[i] <0 or dy[i] < 0 :
            if dx[i] < 0 :
                k = x
            else :
                k= y 
            for m in range(1,k+1) :
                
                if matrix[x+dx[i] * m][y+dy[i]*m] == 'S' :
                    O.append([[x+dx[i]*m -dx[i] , x+dx[i]] ,[y+dy[i]*m - dy[i] , y +dy[i] ] ] )
                    break
                    # matrix[x+dx[i] * m][y+dy[i]*m] = 'C'
                    # pass
        elif dx[i] >0  or dy[i] >0 :
            if dx[i] > 0 :
                k = x
            else :
                k = y
            for m in range(1,n-k) :
                
                if matrix[x+dx[i] * m] [y + m * dy[i]] == 'S' :
                    O.append([[x+dx[i] , x+dx[i] * m -dx[i]]  , [y+dy[i] , y+dy[i] * m -dy[i] ]])
                    break# matrix[x+dx[i] * m][y+dy[i]*m] = 'C'
                    # pass
# for i in matrix:
#     print(i)

print(O)
# print(matrix)