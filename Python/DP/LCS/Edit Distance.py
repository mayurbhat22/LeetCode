#Link: https://leetcode.com/problems/edit-distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = solve(i-1, j-1)
            else:
                dp[i][j] = min(solve(i-1, j-1), solve(i-1, j), solve(i, j-1)) + 1
            return dp[i][j]

        return solve(m-1, n-1)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[m][n]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = [0] * (n+1)
        for j in range(n+1):
            prev[j] = j

        for i in range(1, m+1):
            curr = [i] * (n+1)
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = min(prev[j-1], prev[j], curr[j-1]) + 1
            prev = curr
            
        return prev[n]