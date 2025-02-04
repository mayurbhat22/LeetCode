#Link: https://leetcode.com/problems/car-pooling/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        minHeap = []
        occupied_capacity = 0

        for trip in trips:
            while minHeap and minHeap[0][0] <= trip[1]:
                occupied_capacity -= heapq.heappop(minHeap)[1]
            heapq.heappush(minHeap, (trip[2], trip[0]))
            occupied_capacity += trip[0]
            if occupied_capacity > capacity:
                return False
            
        return True