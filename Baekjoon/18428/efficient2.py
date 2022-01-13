import itertools
import sys
import pprint
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
    if count_O < 0 :
        break
    for i in range(4) :
        if not(x + dx[i] >= 0 and x +dx[i] < n and y + dy[i] >=0 and y+dy[i] < n) :
            continue
        alloc = None
        if dx[i] <0 or dy[i] < 0 :
            if dx[i] < 0 :
                k = x
            else :
                k= y 
            for m in range(1,k+1) :
                if matrix[x+dx[i] * m][y+dy[i]*m] == 'S' :
                    alloc = [[x+dx[i]*m -dx[i] , x+dx[i]] ,[y+dy[i]*m - dy[i] , y +dy[i] ] ]
                    break
        elif dx[i] >0  or dy[i] >0 :
            if dx[i] > 0 :
                k = x
            else :
                k = y
            for m in range(1,n-k) :
                if matrix[x+dx[i] * m] [y + m * dy[i]] == 'S' :
                    alloc =  [[x+dx[i] , x+dx[i] * m -dx[i]]  , [y+dy[i] , y+dy[i] * m -dy[i] ]]
                    break# matrix[x+dx[i] * m][y+dy[i]*m] = 'C'
        if alloc is not None :
            if alloc[0][0] > alloc[0][1] or alloc[1][0] > alloc[1][1] :
                count_O = -1
                break
            flag = False
            for i in range(len(O)) :
                x1,y1 = O[i]
                if max(alloc[0][0] , x1[0] ) <= min(alloc[0][1] , x1[1])  and \
                    max(alloc[1][0] , y1[0] ) <= min(alloc[1][1] , y1[1]):
                    flag = True
                    O[i][0]  = [max(alloc[0][0] , x1[0] ) , min(alloc[0][1] , x1[1])]
                    O[i][1]  = [max(alloc[1][0] , y1[0] ) , min(alloc[1][1] , y1[1])]
                    break
            if not flag and count_O > 0 :
                O.append(alloc)
                count_O-=1
            elif not flag and count_O<=0:
                count_O-=1
                break
if count_O < 0 :
    print('NO')
else :
    print('YES')
