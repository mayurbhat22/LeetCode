#Link: https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        def solve(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if dp[i] != -1:
                return dp[i]
            res = 0
            for j in range(i, min(i+2,n)):
                if int(s[i:j+1]) <= 26:
                    res += solve(j+1)

            dp[i] = res
            return dp[i]
        return solve(0)

