#User function Template for python3
import copy
class Solution:
    def __init__(self):
        self.ans=[]
        self.sol=[]
        self.chess = []
        # self.dx = [1,1,0,-1, 1,-1,-1,0]
        # self.dy = [0,1,1, 1,-1, 0,-1,-1]
        self.dx=[0,-1,1]
        self.dy=[-1,-1,-1]

    # def check(self,x,y) :
    #     for c,r in enumerate(self.ans) :
    #         r-=1
    #         if r==x :
    #             return False
    #     for c,r in enumerate(self.ans) :
    #         r-=1
    #         for i , (delx , dely) in enumerate(zip(self.dx,self.dy)) :
    #             newx = x + delx 
    #             newy = y + dely
    #             while newx < len(self.chess) and newy <len(self.chess) \
    #                 and newx>=0  and newy>=0 :
    #                 if newx == r and newy == c:
    #                     return False
    #                 newx +=delx
    #                 newy += dely
    #     return True
    def check(self,x,y) :
        alpha1 = y-x
        alpha2 = y+x
        for c, r in enumerate(self.ans) :
            r-=1
            if r == x :
                return False
            if -r + alpha2 == c :
                return False
            if r + alpha1 == c:
                return False
        return True
    def makesol(self) :
        if len(self.ans) == len(self.chess) :
            self.sol.append(copy.deepcopy(self.ans))
            return
        for i in range(len(self.chess)) :
            # x , y = i //n , i % n 
            x , y = i , len(self.ans)
            
 
            if self.check(x,y) : 
                self.ans.append(i+1)  
                self.makesol()
                self.ans.pop()
            
        
    def nQueen(self, n):
        self.chess = [[False for _ in range(n)] for _ in range(n)]

        self.makesol()
        self.sol.sort()
        return self.sol
        # code here
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends