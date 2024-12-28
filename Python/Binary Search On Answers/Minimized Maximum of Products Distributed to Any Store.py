#Link: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low, high = 1, max(quantities)
        ans = 0

        def distributionPossible(maxNumber):
            count = 0
            for q in quantities:
                num = q // maxNumber
                q = q - (num * maxNumber)
                if q > 0:
                    count += 1
                count += num
            return count <= n

        while low <= high:
            mid = low + (high - low) // 2
            if(distributionPossible(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans