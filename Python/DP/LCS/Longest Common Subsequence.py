#Link: https://leetcode.com/problems/longest-common-subsequence/
#Top-Down
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + solve(i-1, j-1)
            else:
                dp[i][j] = max(solve(i, j-1), solve(i-1, j))
            return dp[i][j]
        return solve(m-1, n-1)

#Bottom Up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        LCS = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    LCS[i][j] = 1 + LCS[i-1][j-1]
                else:
                    LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

        return LCS[m][n]

#Space Optimization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0] * (n+1)
        for i in range(1, m+1):
            curr = [0] * (n+1)
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(curr[j-1], prev[j])
            prev = curr

        return curr[n]
    