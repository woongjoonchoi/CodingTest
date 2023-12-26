import copy
import time

#  line 19.21.23.24.25.26
# 기존 chk 라는 outer scope의 name을 사용
# recursion의 정의 위배 , 매번 다른 input에 대해 
# 고침, chk-> safety

class Solution:
    def nQueen(self, n):


        ans= []
        chk = {}
        for i in range(1,n+1) :
            chk[i] = set()
        def recur_q(steps,sol,safety) :
            if steps == n :
                ans.append(sol)
                return
            for i in range(1,n+1) :
                if i in safety[steps+1]  : continue
                
                dcp_chk = copy.deepcopy(safety)
                for k in range(steps+2,n+1) :
                    dcp_chk[k].add(i)
                    dcp_chk[k].add(i+(k-(steps+1) ) )
                    dcp_chk[k].add(i-(k-(steps+1) ))
                recur_q(steps+1,sol+[i],dcp_chk)
        recur_q(0,[],chk)
        return ans
    
start = time.time()
ob =Solution()

ans = ob.nQueen(10)
end= time.time()

print(len(ans))
print("time : {}".format(end-start))