#Link: https://leetcode.com/problems/min-cost-climbing-stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n+1)
        def dp(i):
            if i <= 1:
                return 0
            if memo[i] != -1:
                return memo[i]
            one_step = cost[i-1] + dp(i-1)
            two_step = cost[i-2] + dp(i-2)
            
            memo[i] = min(one_step, two_step)
            return memo[i]
        
        return dp(n)

