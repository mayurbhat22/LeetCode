#Link: https://leetcode.com/problems/minimum-time-to-complete-trips/
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low, high = min(time), totalTrips * min(time)
        ans = 0

        def tripsPossible(minTime):
            trips_count = 0
            for t in time:
                trips_count += floor(minTime // t)
            
            return trips_count >= totalTrips
            #     return True
            # else:
            #     return False

        while low <= high:
            mid = low + (high - low) // 2
            if(tripsPossible(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans