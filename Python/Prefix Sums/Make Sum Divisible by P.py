#Link: https://leetcode.com/problems/make-sum-divisible-by-p/
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        if total_sum % p == 0:
            return 0

        k = total_sum % p
        curr_sum = 0
        min_len = len(nums)
        hash_map = {0:-1}

        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            prefix_sum = (curr_sum + p - k) % p
            if prefix_sum in hash_map:
                min_len = min(min_len, i - hash_map[prefix_sum])
        
            hash_map[curr_sum] = i
        return min_len if min_len != len(nums) else -1
