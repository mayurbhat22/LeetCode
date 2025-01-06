#Link: https://leetcode.com/problems/count-the-number-of-good-subarrays/
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        hash_map = {}
        l_slow = l_fast = 0
        pairs = 0
        ans = 0

        for r in range(len(nums)):
            num = nums[r]
            if num in hash_map:
                pairs += hash_map[num]
                hash_map[num] += 1
            else:
                hash_map[num] = 1 
                
            while pairs >= k:
                hash_map[nums[l_fast]] -= 1
                pairs -= hash_map[nums[l_fast]]
                l_fast += 1
            ans += l_fast - l_slow 
        return ans