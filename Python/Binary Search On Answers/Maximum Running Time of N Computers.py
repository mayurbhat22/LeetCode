#Link: https://leetcode.com/problems/maximum-running-time-of-n-computers/
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        totalSum = sum(batteries)
        low, high = 1, totalSum
        ans = 0

        def runTimePossible(maxTime):
            remaining_sum = totalSum
            extraTime = requiredTime = 0
            for i in range(n):
                if maxTime > batteries[i]:
                    requiredTime += maxTime - batteries[i] 
                else:
                    extraTime += maxTime - batteries[i]
                remaining_sum -= batteries[i]
            print(requiredTime, maxTime)
            return requiredTime <= remaining_sum

        while low <= high:
            mid = low + (high-low) // 2
            if(runTimePossible(mid)):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans