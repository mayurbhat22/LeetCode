#Link: https://leetcode.com/problems/kth-smallest-subarray-sum
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        low, high = min(nums), sum(nums)
        ans = 0

        def smallestSubarrayPossible(x):
            l = 0
            cur_sum = count = 0
            for r in range(len(nums)):
                cur_sum += nums[r]
                while cur_sum > x:
                    cur_sum -= nums[l]
                    l += 1
                count += r - l + 1
            return count >= k

        while low<=high:
            mid = low + (high-low) // 2
            if(smallestSubarrayPossible(mid)):
                high = mid - 1
            else:
                low = mid + 1
        
        return low