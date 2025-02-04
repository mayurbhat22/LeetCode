#Link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        total_sum = 0
        res = float('inf')
        maxHeap = []

        for ratio, q in workers:
            heapq.heappush(maxHeap, -q)
            total_sum += q
            if len(maxHeap) > k:
                total_sum += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                res = min(res, total_sum * ratio)
        return res