class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if j < 0:
                return 1
            if i < 0 and j >= 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = solve(i-1, j) + solve(i-1, j-1)
            else:
                dp[i][j] = solve(i-1, j)
            return dp[i][j]

        return solve(m-1, n-1)
        
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        prev = [0] * (n+1)
        prev[0] = 1
        for i in range(1, m+1):
            curr = [0] * (n+1)
            curr[0] = 1
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j] + prev[j-1]
                else:
                    curr[j] = prev[j]
            prev = curr
        return curr[n]
