#Link: https://leetcode.com/problems/maximum-earnings-from-taxi/
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        n = len(rides)
        dp = [-1] * n

        def binarySearch(i):
            l, r = 0, i
            ans = -1

            while l <= r:
                mid = (l + r) // 2
                if rides[mid][1] <= rides[i][0]:
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
            j = binarySearch(i)
            pick = f(j) + rides[i][1] - rides[i][0] + rides[i][2]

            dp[i] = max(notPick, pick)
            return dp[i]

        return f(n-1)