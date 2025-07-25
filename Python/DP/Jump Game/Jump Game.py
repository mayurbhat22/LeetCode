#Link: https://leetcode.com/problems/jump-game/
#DP method
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1] * n

        def solve(i):
            if i >= n-1:
                return True
            if dp[i] != -1:
                return dp[i]
            for jump in range(1, nums[i]+1):
                if solve(i+jump):
                    dp[i] = 1
                    return True
            dp[i] = 0
            return False

        return solve(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n

        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i] = 1
                continue
            for index in range(1, nums[i]+1):
                if i + index >= n-1 or dp[i + index]:
                    dp[i] = 1
                    break

        return True if dp[0] else False

 #Greedy Method        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1

        for i in range(n-2, -1, -1):
            for index in range(nums[i], 0, -1):
                if i + index >= goal:
                    goal = i
                    break

        return goal == 0
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1

        for i in range(n-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
