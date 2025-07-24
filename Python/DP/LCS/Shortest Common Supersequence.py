#Link: https://leetcode.com/problems/shortest-common-supersequence/
# Will give Memory Limit Exceeded, even with Tabulation
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if j >= n:
                return str1[i:]
            if i >= m:
                return str2[j:]
            if dp[i][j] != -1:
                return dp[i][j]

            subsequence_1 = ""
            subsequence_2 = ""

            if str1[i] == str2[j]:
                subsequence = str1[i] + solve(i+1, j+1)
                dp[i][j] = subsequence
            else:
                subsequence_1 = str1[i] + solve(i+1, j)
                subsequence_2 = str2[j] + solve(i, j+1)
                if len(subsequence_1) >= len(subsequence_2):
                    dp[i][j] = subsequence_2
                else:
                    dp[i][j] = subsequence_1
            return dp[i][j]

        return solve(0, 0)

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        
        s = ""
        i, j = m, n

        while(i > 0 and j > 0):
            if str1[i-1] == str2[j-1]:
                s = str1[i-1] + s
                i -= 1
                j -= 1
            elif dp[i-1][j] < dp[i][j-1]:
                s = str1[i-1] + s
                i -= 1
            else:
                s = str2[j-1] + s
                j -= 1
        while(i > 0):
            s = str1[i-1] + s
            i -= 1
        while(j > 0):
            s = str2[j-1] + s
            j -= 1
        
        return s
        

