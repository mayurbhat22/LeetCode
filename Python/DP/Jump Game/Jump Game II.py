class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def solve(i):
            if i >= n-1:
                return 0
            if dp[i] != -1:
                return dp[i]

            min_jumps = float("inf")
            for index in range(1, nums[i]+1):
                min_jumps = min(min_jumps, 1 + solve(i+index))
            dp[i] = min_jumps
            return dp[i]

        return solve(0)

