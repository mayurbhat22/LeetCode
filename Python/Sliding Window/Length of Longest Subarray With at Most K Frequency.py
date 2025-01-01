#Link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        max_len = 0
        hash_map = {}
        for r in range(len(nums)):
            num = nums[r]
            hash_map[num] = hash_map.get(num, 0) + 1
            
            while l<=r and hash_map[num] > k:
                hash_map[nums[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len