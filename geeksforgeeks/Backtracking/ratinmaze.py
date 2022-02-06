#User function Template for python3
import copy
delta_x = [0,1,0,-1]
delta_y = [1,0,-1,0]
direc = ['R' ,'D' , 'L','U']
def check(x,y,n) :
    if x>= 0 and x <n and y>=0 and y<n :
        return True
    return False
class Solution:
    def __init__(self) :
        self.ans = []
        self.path = []
        self.visited=[]

    def solv(self, m,n,x,y) :
        if x == n-1 and y ==n-1 :
            self.ans.append(''.join(copy.deepcopy(self.path)))
            return
        for i, (dx,dy,d) in enumerate(zip(delta_x,delta_y,direc)) :
            if check(x+dx,y+dy,n) and m[x+dx][y+dy] == 1 and not self.visited[x+dx][y+dy]  :
                self.path.append(d)
                self.visited[x+dx][y+dy] = True
                self.solv(m,n,x+dx,y+dy)
                self.path.pop()
                self.visited[x+dx][y+dy] = False
            
    def findPath(self, m, n):
        self.visited = [ [False for _ in range(n)] for _ in range(n)]
        if m[0][0] == 0 :
            return self.ans
        self.visited[0][0] = True
        self.solv(m,n,0,0)
        return self.ans 
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends