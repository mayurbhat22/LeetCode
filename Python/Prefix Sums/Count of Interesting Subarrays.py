#Link: https://leetcode.com/problems/count-of-interesting-subarrays/
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            count[i+1] = count[i] + (1 if nums[i] % modulo == k else 0)
        # print(count)
        res = 0
        count_map = {0:1}

        for i in range(1, len(nums)+1):
            rem = count[i] % modulo
            target = (rem - k + modulo) % modulo
            if target in count_map:
                res += count_map[target]
            count_map[rem] = count_map.get(rem, 0) + 1
        return res