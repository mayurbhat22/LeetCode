#Link: https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
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
            ans = max(ans, r-l+1)
        l = 0
        for r in range(n):
            mid = (nums[r] + nums[l]) // 2

            while mid - nums[l] > k or nums[r] - mid > k:
                l += 1
                mid = (nums[r] + nums[l]) // 2
            ans = max(ans, r-l+1)
        return ans