#Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        res = index = 0
        n = len(events)
        events.sort()

        minHeap = []

        while minHeap or index < n:
            if not minHeap:
                day = events[index][0]
            while index < n and events[index][0] <= day:
                heapq.heappush(minHeap, events[index][1])
                index += 1
            heapq.heappop(minHeap)
            day += 1
            res += 1

            while minHeap and minHeap[0] < day:
                heapq.heappop(minHeap)
        return res