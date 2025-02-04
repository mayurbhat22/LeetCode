#Link: https://leetcode.com/problems/furthest-building-you-can-reach/
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []

        for i in range(len(heights)-1):
            d = heights[i+1] - heights[i]
            if d > 0:
                heapq.heappush(minHeap, d)
            if len(minHeap) > ladders:
                bricks -= heapq.heappop(minHeap)
            if bricks < 0:
                return i
        return len(heights) - 1