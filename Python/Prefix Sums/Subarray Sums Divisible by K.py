#Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        map = {}
        map[0] = 1
        res , curr_sum = 0, 0
        for num in nums:
            curr_sum += num
            if curr_sum % k in map:
                res += map[curr_sum % k]
                map[curr_sum % k] += 1
            else:
                map[curr_sum % k] = 1
        return res