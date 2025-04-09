#Link: https://leetcode.com/problems/maximum-population-year/
from sortedcontainers import SortedDict
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        popluation = [0] * (2051 - 1950)
        max_population = 0
        max_population_year = 0
        freq = 0
        for l in logs:
            popluation[l[0]-1950] += 1
            popluation[l[1]-1950] -= 1
        
        for i in range(100):
            count = popluation[i]
            freq += count
            if freq > max_population:
                max_population = freq
                max_population_year = i + 1950
        
        return max_population_year