#Link: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n
        LDS = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], 1 + LDS[j])
        
        for i in range(n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        max_height = 0
        for i in range(1, n-1):
            if LIS[i] != 1 and LDS[i] != 1:
                max_height = max(max_height, LIS[i] + LDS[i] - 1)
        
        return n - max_height