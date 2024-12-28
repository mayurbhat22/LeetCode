#Link: https://leetcode.com/problems/minimum-time-to-repair-cars/
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, max(ranks) * cars * cars
        ans = 0

        def repairPossible(maxTime):
            count = 0
            for rank in ranks:
                val = maxTime // rank
                count += floor(sqrt(val))
            return count >= cars

        while low <= high:
            mid = low + (high - low) // 2
            if(repairPossible(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans