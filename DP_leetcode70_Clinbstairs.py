dp = {}
class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        
        # 접근 5 층에 접근전 단계는  5-2 , 5 -1 
        # 즉 DP[n] = dp[n-2] +dp[n-1] 이라는 규칙이 발견 
        # top down 방식
        '''
        if n not in dp:
            dp[n] = Solution.climbStairs(self,n-2) + Solution.climbStairs(self,n-1)
        '''
        # bottom up 방식
        for i in range(3,n+1):
            dp[i] = dp[i-2] +dp[i-1]

        return dp[n]
    
