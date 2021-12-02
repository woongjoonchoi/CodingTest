class Solution:
    dp = []
    def cal_dp(start , end )  :
        sum = 0
        if start >= len(Solution.dp) or end <0 :
            return 1
        if Solution.dp[start][end] != -1:
            return Solution.dp[start][end]
        if start > end :
            return 1
        for i in range(start,end+1):
            sum += Solution.cal_dp(start,i-1) * Solution.cal_dp(i+1,end)
        Solution.dp[start][end]=sum       
        return sum
    def numTrees(self, n: int) -> int:
        Solution.dp  = [  [-1 for _ in range(n)] for _ in range(n)]
        for i in range(n) :
            Solution.dp[i][i] = 1
        Solution.cal_dp(0,n-1)
        return Solution.dp[0][n-1]