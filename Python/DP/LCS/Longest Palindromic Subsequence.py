#https://leetcode.com/problems/longest-palindromic-subsequence
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        def solve(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                dp[i][j] = 2 + solve(i+1, j-1)
            else:
                dp[i][j] = max(solve(i, j-1), solve(i+1, j))
            return dp[i][j]
            
        return solve(0, n-1)

        
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(0, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                if i > j:
                    continue

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        return dp[0][n-1]

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev = [0] * n
        for i in range(n-1, -1, -1):
            curr = [0] * n
            for j in range(0, n):
                if i == j:
                    curr[j] = 1
                    continue
                if i > j:
                    continue

                if s[i] == s[j]:
                    curr[j] = 2 + prev[j-1]
                else:
                    curr[j] = max(curr[j-1], prev[j])
            prev = curr
        return prev[n-1]