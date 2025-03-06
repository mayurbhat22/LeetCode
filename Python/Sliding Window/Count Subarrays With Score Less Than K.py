#Link: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        res = 0
        l = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while l <= r and (curr_sum * (r-l+1)) >= k:
                curr_sum -= nums[l]
                l += 1
            res += r - l + 1
        return res 