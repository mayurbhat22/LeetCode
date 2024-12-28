class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        max_len = 0
        sum = 0

        for r in range(len(nums)):
            sum += nums[r]

            while ((r-l+1) * nums[r]) - sum > k and l < r:
                sum -= nums[l]
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return max_len 