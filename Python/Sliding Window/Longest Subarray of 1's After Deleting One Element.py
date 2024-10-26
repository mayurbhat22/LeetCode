class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        max_len = 0
        k = 1

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            
            while k < 0 and l < r:
                if nums[l] == 0:
                    k += 1
                l += 1
            max_len = max(max_len, r - l)
        
        return max_len