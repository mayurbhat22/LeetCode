#Link: https://leetcode.com/problems/maximum-length-of-pair-chain/
#Memoization
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        LIS = [[-1] * (n+1) for _ in range(n)]

        def solve(i, prev_index):
            if i == n:
                return 0
            if LIS[i][prev_index+1] != -1:
                return LIS[i][prev_index+1]
            skip = solve(i+1, prev_index)
            pick = 0
            if prev_index == -1 or pairs[prev_index][1] < pairs[i][0]:
                pick = 1 + solve(i+1, i)
            
            LIS[i][prev_index+1] = max(skip, pick)
            return LIS[i][prev_index+1]

        return solve(0, -1)
    
#Tabulation
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