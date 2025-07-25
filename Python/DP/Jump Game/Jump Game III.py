class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        dp = [-1] * n

        def solve(i):
            if i < 0 or i >= n:
                return False
            if arr[i] == 0:
                return True
            if dp[i] != -1:
                return dp[i]

            move_front = solve(i+arr[i])
            dp[i] = move_front
            move_back = solve(i-arr[i])

            dp[i] = move_back or move_front
            return dp[i]

        return solve(start)