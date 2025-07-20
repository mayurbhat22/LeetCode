class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def dp(i):
            if i == 0:
                return nums[i]
            if memo[i] != -1:
                return memo[i]
            leave_house = dp(i-1)
            rob_house = nums[i]
            if i > 1:
                rob_house += dp(i-2)

            memo[i] = max(leave_house, rob_house)
            return memo[i]
        
        return dp(n-1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n
        memo[0] = nums[0]
        for i in range(1, n):
            leave_house = memo[i-1]
            rob_house = nums[i]
            if i > 1:
                rob_house += memo[i-2]
            memo[i] = max(leave_house, rob_house)
        
        return memo[n-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev_1 = nums[0]
        prev_2 = 0
        for i in range(1, n):
            leave_house = prev_1
            rob_house = nums[i]
            if i > 1:
                rob_house += prev_2
            curr = max(leave_house, rob_house)
            prev_2 = prev_1
            prev_1 = curr
        return prev_1