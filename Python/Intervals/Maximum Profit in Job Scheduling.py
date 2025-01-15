#Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        sorted_data = sorted(zip(endTime, startTime, profit), key=lambda x: x[0])
        endTime, startTime, profit = map(list, zip(*sorted_data))

        print(startTime, endTime, profit)

        dp = [-1] * n

        def binarySearch(i):
            l, r = 0, n
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if endTime[mid] <= startTime[i]:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        def f(i):
            if i < 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            notPick = f(i-1)
            pick = 0
            j = binarySearch(i)
            pick = f(j) + profit[i]
            
            dp[i] = max(pick, notPick)
            return dp[i]

        return f(n-1)