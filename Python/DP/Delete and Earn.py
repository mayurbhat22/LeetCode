#Link: https://leetcode.com/problems/delete-and-earn
#Top-Down
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        LIS = [-1] * (max_number+1)

        def solve(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            if LIS[num] != -1:
                return LIS[num]
            skip = solve(num-1)
            pick = points[num] + solve(num-2)

            LIS[num] = max(pick, skip)
            return LIS[num]
        return solve(max_number)

#Bottom-Up
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        LIS = [0] * (max_number+1)
        LIS[1] = points[1]

        for num in range(2, max_number+1):
            LIS[num] = max(LIS[num-1], LIS[num-2] + points[num])
        
        return LIS[max_number]
    