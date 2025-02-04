#Link: https://leetcode.com/problems/minimum-cost-to-connect-sticks/
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minHeap = [i for i in sticks]
        heapq.heapify(minHeap)

        total_sum = 0
        
        while len(minHeap) > 1:
            first_ele = heapq.heappop(minHeap)
            second_ele = heapq.heappop(minHeap)
            total_sum += first_ele + second_ele
            heapq.heappush(minHeap, first_ele + second_ele)
        return total_sum