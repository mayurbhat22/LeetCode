class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[[-1] * (n+1) for _ in range(n)] for _ in range(n)]

        def solve(i, j, prev):
            if i >= j:
                return 0
            if dp[i][j][prev+1] != -1:
                return dp[i][j][prev+1]
            if s[i] == s[j]:
                palindrome_length = solve(i+1, j-1, i)
                if prev == -1 or s[i] != s[prev]:
                    palindrome_length += 2
                dp[i][j][prev+1] = palindrome_length
            else:
                dp[i][j][prev+1] = max(solve(i+1, j, prev), solve(i, j-1, prev))
            return dp[i][j][prev+1]

        return solve(0, n-1, -1)