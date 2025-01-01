#Link: https://leetcode.com/problems/find-the-longest-equal-subarray/
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        max_len = max_val = 0
        hash_map = {}
        for r in range(len(nums)):
            num = nums[r]
            hash_map[num] = hash_map.get(num, 0) + 1
            
            curr_sum = r - l + 1
            max_val = max(max_val, hash_map[num])
            while l<=r and curr_sum - max_val > k:
                hash_map[nums[l]] -= 1
                curr_sum -= 1
                l += 1

            max_len = max(max_len, max_val)
        
        return max_len