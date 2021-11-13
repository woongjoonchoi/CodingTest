class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9) :
            c_s = set()
            r_s = set()
            r_count , c_count = 0 , 0
            for j in range(9) :
                if board[j][i] != '.' :
                    c_s.add(board[j][i])
                    c_count+=1
                if board[i][j] != '.' :
                    r_s.add(board[i][j])
                    r_count+=1
            if r_count != len(r_s) :
                return False
            if c_count  != len(c_s) :
                return False
        for k in range(3) :
            for v in range(3) :
                s = set()
                count = 0
                for i in range(3) :
                    for j in range(3) :
                        if board[k*3+i][v*3+j] != '.' :
                            s.add(board[k*3+i][v*3+j])
                            count+=1
                if len(s) != count :
                    return False
        return True