#Link: https://leetcode.com/problems/maximum-length-of-pair-chain/
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        LIS = [1] * n
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if pairs[i][1] < pairs[j][0]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
            res = max(res, LIS[i])
        return res