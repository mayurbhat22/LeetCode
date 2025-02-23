#Link: https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        index_map = {0 : -1}
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            mod_val = curr_sum%k
            if mod_val in index_map:
                if i - index_map[mod_val] >= 2:
                    return True
            else:
                index_map[mod_val] = i
        return False