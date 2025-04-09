#Link: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        count = [0] * 52
        for r in ranges:
            count[r[0]] += 1
            count[r[1]+1] -= 1
        
        freq = 0
        i = 0
        while i <= right:
            while left <= i <= right:
                freq += count[i]
                if freq <= 0:
                    return False
                i += 1
            freq += count[i]
            i += 1
        return True