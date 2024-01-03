#User function Template for python3
import time

class Solution:
    def nQueen(self, n):
        # code here
        # board = [[0] * n  for _ in range(n) ] 
        ans= []
        chk = {}
        for i in range(1,n+1) :
            chk[i] = 0
        def recur_q(steps,sol) :
            if steps == n :
                for i,t in enumerate(sol) :
                    for k in range(i+1,len(sol)) :
                        if sol[k] == t or sol[k] == t + (k-i) or sol[k] == t - (k-i) :
                            break
                    else :
                        continue
                    break 
                else :
                    ans.append(sol)
                return
            
            for i in range(1,n+1) :
                if chk[i] == 1 : continue
                chk[i] = 1
                recur_q(steps+1,sol+[i])
                chk[i] = 0
        recur_q(0,[])
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
        
#         ob = Solution()
#         ans = ob.nQueen(n)
#         if(len(ans) == 0):
#             print("-1")
#         else:
#             for i in range(len(ans)):
#                 print("[",end="")
#                 for j in range(len(ans[i])):
#                     print(ans[i][j],end = " ")
#                 print("]",end = " ")
#             print()
                
# } Driver Code Ends


start = time.time()
ob =Solution()

ans = ob.nQueen(10)
end= time.time()
print(len(ans))
print(ans)
print("time : {}".format(end-start))