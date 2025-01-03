class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_len = 0
        k = 1
        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            while l < r and k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len