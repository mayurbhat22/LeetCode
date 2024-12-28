#Link: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)
        ans = 0

        def operationsPossible(maxBalls):
            operations = 0
            for num in nums:
                if num > maxBalls:
                    if num % maxBalls == 0:
                        operations += (num / maxBalls) - 1
                    else:
                        operations += num // maxBalls
            return operations <= maxOperations

        while low <= high:
            mid = low + (high - low) // 2
            if(operationsPossible(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans