#Link: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        index_map = {0:-1}
        max_length = curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            diff = curr_sum - k

            if diff in index_map:
                max_length = max(max_length, i - index_map[diff])
            if not(curr_sum in index_map):
                index_map[curr_sum] = i
        return max_length