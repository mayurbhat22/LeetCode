#Link: https://leetcode.com/problems/zero-array-transformation-i/
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        count = [0] * (len(nums)+1)

        for q in queries:
            count[q[0]] += 1 
            count[q[1]+1] -= 1
        
        curr_freq = 0
        for i, num in enumerate(nums):
            curr_freq += count[i]
            if num > curr_freq:
                return False
        return True