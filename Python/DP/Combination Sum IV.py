#Link: https://leetcode.com/problems/combination-sum-iv
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1] * (target+1) for _ in range(n)]
        def solve(i, target):
            if target == 0:
                return 1
            if i >= n:
                return 0
            if dp[i][target] != -1:
                return dp[i][target]
            res = 0
            for index in range(n):
                if target >= nums[index]:
                    target -= nums[index]
                    res += solve(index, target)
                    target += nums[index]
            dp[i][target] = res   
            return dp[i][target]

        return solve(0, target)