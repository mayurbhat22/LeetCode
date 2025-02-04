#Link: https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []
        for ele, cnt in count.items():
            heapq.heappush(min_heap, (cnt, ele))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = [ele for cnt, ele in min_heap]
        return res