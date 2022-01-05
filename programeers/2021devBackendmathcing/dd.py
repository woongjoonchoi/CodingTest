def solution(rows, columns, queries):
    answer = []
    cnt = 0
    mat = [[i*columns + j for j in range(1,columns+1) ] for  i in range(rows)]  
    for i in mat :
        print(i)
    for q in queries:
        x1,y1,x2,y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        tmp = mat[x1][y2]
        tmp2 = mat[x2][y1]
        for i in range(y1,y2) :
            mat[x1][y1+y2-i] = mat[x1][y1+y2-i-1]
            mat[x2][i]=mat[x2][i+1]

        for i in range(x1+1,x2) :
            mat[i-1][y1] = mat[i][y1]
            mat[x1+x2+1-i][y2] = mat[x1+x2-i][y2]
        mat[x1+1][y2] = tmp
        mat[x2-1][y1] = tmp2
        print(' ')
        for i in mat :
            print(i)
        
    return answer

solution(	6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])