#Link: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        l, r = 0, 0
        ans = 0
        n = len(nums)
        count = Counter(nums)

        for mid in range(n):
            while nums[mid] - nums[l] > k:
                l += 1
            
            while r < n-1 and nums[r+1] - nums[mid] <= k:
                r += 1
            total = r - l + 1
            ans = max(ans, min(total - count[nums[mid]], numOperations) + count[nums[mid]])
        l = 0
        for r in range(n):
            mid = (nums[r] + nums[l]) // 2

            while mid - nums[l] > k or nums[r] - mid > k:
                l += 1
                mid = (nums[r] + nums[l]) // 2
            ans = max(ans, min(r-l+1, numOperations))
        
        return ans