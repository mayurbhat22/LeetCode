#Link: https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: list[int]) -> int:
        # code here
        minHeap = [i for i in arr]
        heapq.heapify(minHeap)

        total_sum = 0
        
        while len(minHeap) > 1:
            first_ele = heapq.heappop(minHeap)
            second_ele = heapq.heappop(minHeap)
            total_sum += first_ele + second_ele
            heapq.heappush(minHeap, first_ele + second_ele)
        return total_sum
