#Link: https://leetcode.com/problems/longest-increasing-subsequence
#Memoization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n)]

        def solve(i, prev_ele):
            if i == n-1:
                return 1 if nums[i] > nums[prev_ele] or prev_ele == -1 else 0
            if dp[i][prev_ele+1] != -1:
                return dp[i][prev_ele+1]
            skip = solve(i+1, prev_ele)
            pick = 0
            if prev_ele == -1 or nums[i] > nums[prev_ele]:
                pick = 1 + solve(i+1, i)
            
            dp[i][prev_ele+1] = max(skip, pick)
            return dp[i][prev_ele+1]

        return solve(0, -1)

#Binary Search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [nums[0]]
        res = 1
        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                res += 1
            else:
                index = bisect_left(temp, nums[i])
                temp[index] = nums[i]
        return res