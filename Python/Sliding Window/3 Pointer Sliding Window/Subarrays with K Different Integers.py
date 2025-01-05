#Link: https://leetcode.com/problems/subarrays-with-k-different-integers/
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left_slow, left_fast = 0, 0
        res, count = 0, 0
        map = {}
        for right in range(len(nums)):
            map[nums[right]] = map.get(nums[right], 0) + 1
            if map[nums[right]] == 1:
                count += 1

            while count > k:
                map[nums[left_fast]] -= 1
                if map[nums[left_fast]] == 0:
                        count -= 1
                left_fast += 1
                left_slow = left_fast

            if count == k:
                while map[nums[left_fast]] != 1:
                    map[nums[left_fast]] -= 1
                    if map[nums[left_fast]] == 0:
                        count -= 1
                    left_fast += 1
                res += left_fast - left_slow + 1
        return res

