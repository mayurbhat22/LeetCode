#Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[-1] * k for _ in range(n)]

        def binarySearch(i):
            l, r = 0, n
            ans = -1
            while l<=r:
                mid = (l+r) // 2
                if events[mid][1] < events[i][0]:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        def f(i, count):
            if count == k or i < 0:
                return 0

            if dp[i][count] != -1:
                return dp[i][count]
            notPick = f(i-1, count)
            pick = 0
            j = binarySearch(i)
            pick = f(j, count+1) + events[i][2]
            
            dp[i][count] = max(pick, notPick)
            return dp[i][count]

        return f(n-1, 0)