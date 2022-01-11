import itertools
import sys
n = int(sys.stdin.readline())
# print(n)
matrix =[]
S = []
T = []
O = []
for i in range(n) :
    matrix.append(sys.stdin.readline().rstrip().split())
    
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 'T' :
            T.append((i,j))
        elif matrix[i][j] == 'S':
            S.append((i,j))
        else :
            O.append((i,j))
count = 0
for om in itertools.combinations(O,3):
    count = 0
    for t in T :
        for s in S :
            for o in om:      
                if  (t[0] == s[0] and (o[0] != t[0] or 
                    ( o[1] >max(t[1] , s[1]) or o[1] < min(t[1] ,s[1]))))\
                    or (t[1] == s[1] and (o[1] != t[1] or 
                     (o[0] > max(t[0] ,s[0]) or o[0] < min(t[0] , s[0])))):
                    pass
                else :
                    count+=1
                    break
    if count == len(T) * len(S) :
        break
    
if count == len(T) * len(S) : print('YES')
else : print('NO')
