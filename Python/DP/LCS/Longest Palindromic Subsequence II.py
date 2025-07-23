class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[[-1] * (27) for _ in range(n)] for _ in range(n)]

        def solve(i, j, prev):
            if i >= j:
                return 0
            if dp[i][j][prev] != -1:
                return dp[i][j][prev]
            if s[i] == s[j]:
                palindrome_length = solve(i+1, j-1, ord(s[i]) - ord('a'))
                if prev == "" or ord(s[i]) - ord('a') != prev:
                    palindrome_length += 2
                dp[i][j][prev] = palindrome_length
            else:
                dp[i][j][prev] = max(solve(i+1, j, prev), solve(i, j-1, prev))
            return dp[i][j][prev]

        return solve(0, n-1, 26)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[[0] * (27) for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                for prev in range(26, -1, -1):
                    if s[i] == s[j]:
                        palindrome_length = dp[i+1][j-1][ord(s[i]) - ord('a')]
                        if prev == 26 or ord(s[i]) - ord('a') != prev:
                            palindrome_length += 2
                        dp[i][j][prev] = palindrome_length
                    else:
                        dp[i][j][prev] = max(dp[i+1][j][prev], dp[i][j-1][prev])

        return dp[0][n-1][26]