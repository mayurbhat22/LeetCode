#Link: https://leetcode.com/problems/integer-break/
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [[-1] * (n+1) for _ in range(n+1)]

        def solve(n, k):
            if k == 1:
                return n
            if dp[n][k] != -1:
                return dp[n][k]
            res = 1
            max_product = 0
            for i in range(2, max(3, k)):
                for num in range(1, n):
                    if num <= n:
                        res = num * solve(n-num, i-1)
                        max_product = max(max_product, res)

            dp[n][k] = max_product
            return dp[n][k]

        return solve(n, n)