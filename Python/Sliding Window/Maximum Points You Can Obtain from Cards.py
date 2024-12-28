#Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints)
        l = 0
        n = len(cardPoints)
        minSum = float("inf")
        currSum = 0
        for r in range(n):
            currSum += cardPoints[r]

            if r - l + 1 == n-k:
                minSum = min(minSum, currSum)
                currSum -= cardPoints[l]
                l += 1
        minSum = 0 if minSum == float("inf") else minSum
        return totalSum - minSum