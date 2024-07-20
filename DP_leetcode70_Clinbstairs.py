class Solution(object):
    def climbStairs(self, n):
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(n+1):
            if i not in dp:
                dp[i] = Solution.climbStairs(self,n-2) + Solution.climbStairs(self,n-1)

        return dp[n]
        