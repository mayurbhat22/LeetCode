#Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        required_sum = total_sum - x
        if required_sum == 0:
            return len(nums)
        curr_sum = 0
        max_len = 0
        hash_map = {0:-1}
        for i, num in enumerate(nums):
            curr_sum += num
            diff = curr_sum - required_sum
            if diff in hash_map:
                print(diff)
                max_len = max(max_len, i - hash_map[diff])
            if curr_sum not in hash_map:
                hash_map[curr_sum] = i
        return len(nums) - max_len if max_len else -1