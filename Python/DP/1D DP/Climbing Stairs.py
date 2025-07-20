#Link: https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        def dp(n):
            if n == 0 or n == 1:
                return 1
            if memo[n] != -1:
                return memo[n]
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        
        return dp(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]