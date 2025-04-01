#Link: https://leetcode.com/problems/solving-questions-with-brainpower/
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1] * n
        def max_points(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            skip = max_points(i+1)
            solve = questions[i][0] + max_points(i + questions[i][1] + 1)

            dp[i] = max(solve, skip)
            return dp[i]

        return max_points(0)