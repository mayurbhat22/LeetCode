#Link: https://leetcode.com/problems/last-stone-weight/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if x == y:
                continue
            else:
                heapq.heappush(maxHeap, x - y)
        return -maxHeap[0] if maxHeap else 0