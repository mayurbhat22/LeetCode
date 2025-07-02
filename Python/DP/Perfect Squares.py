#Link: https://leetcode.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n+1)

        def solve(n):
            if n == 0:
                return 0
            if n < 0:
                return float("inf")
            if dp[n] != -1:
                return dp[n]
            res = 0
            min_res = float("inf")
            for num in range(floor(sqrt(n)), 0, -1):
                if num * num <= n:
                    res = 1 + solve(n - (num * num))
                    min_res = min(min_res, res) 
            dp[n] = min_res
            return dp[n]

        return solve(n)