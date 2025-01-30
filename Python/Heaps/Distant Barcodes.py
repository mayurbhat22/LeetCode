#Link: https://leetcode.com/problems/distant-barcodes/
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        maxHeap = [(-f, num) for num, f in count.items()]
        heapq.heapify(maxHeap)
        res = []
        while maxHeap:
            temp = {}
            for _ in range(2):
                if maxHeap:
                    f, num = heapq.heappop(maxHeap)
                    temp[num] = -f
                    res.append(num)
            
            for num, f in temp.items():
                if f - 1 > 0:
                    heapq.heappush(maxHeap, (-(f-1), num))
        return res