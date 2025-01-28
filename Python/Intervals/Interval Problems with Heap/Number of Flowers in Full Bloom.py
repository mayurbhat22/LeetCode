#Link: https://leetcode.com/problems/number-of-flowers-in-full-bloom/
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p,i) for i, p in enumerate(people)]
        flowers.sort()
        res = [0] * len(people)
        end = []
        n = len(flowers)
        j = 0
        for p, i in sorted(people):
            while j < n and flowers[j][0] <= p:
                heapq.heappush(end, flowers[j][1])
                j += 1
            
            while end and end[0] < p:
                heapq.heappop(end)
            res[i] = len(end)
        return res