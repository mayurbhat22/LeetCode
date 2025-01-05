#Link: https://leetcode.com/problems/count-number-of-nice-subarrays/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left_slow, left_fast = 0, 0
        res, odd = 0, 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1
            while odd > k:
                if nums[left_fast] % 2 == 1:
                    odd -= 1
                left_fast += 1
                left_slow = left_fast
            if odd == k:
                while left_fast <= right and nums[left_fast] % 2 != 1:
                    left_fast += 1
                res += left_fast - left_slow + 1
        
        return res