#Link: https://leetcode.com/problems/maximum-alternating-subarray-sum/
class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        pos = neg = max_sum = float("-inf")

        for num in nums:
            pos, neg = max(neg + num, num), pos - num
            max_sum = max(max_sum, pos, neg)

        return max_sum
            