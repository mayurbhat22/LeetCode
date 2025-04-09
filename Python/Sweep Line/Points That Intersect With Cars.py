#Link: https://leetcode.com/problems/points-that-intersect-with-cars/
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        interesction = [0] * 102
        for s, e in nums:   
            interesction[s] += 1
            interesction[e+1] -= 1
        
        res = count = 0

        for i in range(102):
            count += interesction[i]
            if count >= 1:
                res += 1
        return res