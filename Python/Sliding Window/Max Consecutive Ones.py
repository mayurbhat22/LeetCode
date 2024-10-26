class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_len = 0

        while r < len(nums):
            if nums[r] == 0:
                r += 1
                l = r
                continue
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len