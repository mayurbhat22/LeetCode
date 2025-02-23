#Link: https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_map = {0 : 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in count_map:
                count += count_map[diff]
            count_map[curr_sum] = count_map.get(curr_sum, 0) + 1
        return count
