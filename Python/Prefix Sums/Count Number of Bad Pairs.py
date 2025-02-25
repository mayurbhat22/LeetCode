#Link: https://leetcode.com/problems/count-number-of-bad-pairs/
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hash_map = {}
        total_pairs = (len(nums) * (len(nums)-1)) // 2
        good_pairs = 0
        for i, num in enumerate(nums):
            good_pairs += hash_map.get(num-i, 0)
            hash_map[num-i] = hash_map.get(num-i, 0) + 1

        return total_pairs - good_pairs
    

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hash_map = {}
        total_pairs = (len(nums) * (len(nums)-1)) // 2
        res = 0
        for i, num in enumerate(nums):
            hash_map[num-i] = hash_map.get(num-i, 0)
            
        for values in hash_map.values():
            if values >= 2:
                res += (values * (values - 1) ) // 2
        return total_pairs - res