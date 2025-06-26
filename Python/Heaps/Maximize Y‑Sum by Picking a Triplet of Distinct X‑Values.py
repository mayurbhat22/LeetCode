#Link: https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        combined_list = sorted(list(zip(x, y))) #nlogn
        prev_value, max_value = combined_list[0][0], combined_list[0][1]
        max_heap = []

        for i in range(1, n): #n
            if combined_list[i][0] != prev_value:
                heapq.heappush(max_heap, -max_value) #logn
                max_value = combined_list[i][1]
            else:
                max_value = max(max_value, combined_list[i][1])
            prev_value = combined_list[i][0]
        heapq.heappush(max_heap, -max_value)
        if len(max_heap) < 3:
            return -1
        res = 0
        for _ in range(3):
            res += heapq.heappop(max_heap)
        return -res