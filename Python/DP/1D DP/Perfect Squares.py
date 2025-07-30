#Link: https://leetcode.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        def solve(n):
            if n == 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            max_square = floor(sqrt(n))
            res = float("inf")
            for num in range(max_square, 0, -1):
                if num * num <= n:
                    res = min(res, 1 + solve(n - (num*num)))
            dp[n] = res
            return dp[n]

        return solve(n)