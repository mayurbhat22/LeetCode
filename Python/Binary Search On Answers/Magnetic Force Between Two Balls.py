#Link: https://leetcode.com/problems/magnetic-force-between-two-balls/
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 1, max(position)
        ans = 0

        def placementPossible(minDistance):
            count = 1
            prevPosition = position[0]
            for i in range(1, len(position)):
                if position[i] - prevPosition >= minDistance:
                    count += 1
                    prevPosition = position[i]

            return count >= m

        while low <= high:
            mid = low + (high - low) // 2
            if(placementPossible(mid)):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans