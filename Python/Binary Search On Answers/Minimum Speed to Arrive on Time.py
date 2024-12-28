#Link: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low, high = 1, 10 ** 7
        ans = -1

        def timePossible(speed):
            h = 0
            for i in range(len(dist)):
                val = dist[i]/speed
                if i != len(dist)-1:
                    h += ceil(val)
                else:
                    h += val
            return h <= hour

        while low <= high:
            mid = low + (high - low) // 2
            if(timePossible(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans