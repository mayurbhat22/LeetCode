#Link: https://leetcode.com/problems/minimum-interval-to-include-each-query/
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(q, i) for i, q in enumerate((queries))]
        n = len(intervals)
        res = [0] * len(queries)
        intervals.sort()
        minHeap = []
        j = 0
        for q, i in sorted(queries):
            while j < n and intervals[j][0] <= q:
                heapq.heappush(minHeap, (intervals[j][1] - intervals[j][0] + 1, intervals[j][1]))
                j += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[i] = minHeap[0][0] if minHeap else -1 
        return res