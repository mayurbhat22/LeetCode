#Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        if sum(candies) == k:
            return 1
        low, high = 1, max(candies)
        ans = 0

        def distributionPossible(minCandies):
            count = 0
            for c in candies:
                count += c // minCandies
            return count >= k

        while low <= high:
            mid = low + (high - low) // 2
            if(distributionPossible(mid)):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return high