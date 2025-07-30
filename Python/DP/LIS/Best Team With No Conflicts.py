#Link: https://leetcode.com/problems/best-team-with-no-conflicts
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        age_score = sorted(zip(ages, scores))
        dp = [[-1] * (n+1) for _ in range(n)]

        def solve(i, prev):
            if i >= n:
                return 0
            if dp[i][prev+1] != -1:
                return dp[i][prev+1]

            skip = solve(i+1, prev)
            pick = 0
            if prev == -1 or age_score[i][1] >= age_score[prev][1]:
                pick = age_score[i][1] + solve(i+1, i)
            dp[i][prev+1] = max(skip, pick)
            return dp[i][prev+1]

        return solve(0, -1)

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:    
        n = len(ages)
        age_score = sorted(zip(ages, scores))
        dp = [age_score[i][1] for i in range(n)]
        max_score = max(dp)
        for i in range(n-1, -1, -1):
            for prev in range(i+1, n):
                if age_score[prev][1] >= age_score[i][1]:
                    dp[i] = max(dp[i], dp[prev] + age_score[i][1])
                    max_score = max(max_score, dp[i])
        return max_score