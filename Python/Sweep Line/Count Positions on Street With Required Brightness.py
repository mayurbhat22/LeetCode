#Link: https://leetcode.com/problems/count-positions-on-street-with-required-brightness/
from sortedcontainers import SortedDict
class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        for l in lights:
            l[0], l[1] = max(0, l[0] - l[1]), min(n-1, l[0] + l[1])
        brightness = [0] * (n+1)
        for l in lights:
            brightness[l[0]] += 1
            brightness[l[1]+1] -= 1
        print(brightness)
        freq = 0
        res = 0
        for num, count in enumerate(brightness):
            freq += count
            if num < n and freq >= requirement[num]:
                res += 1
        return res