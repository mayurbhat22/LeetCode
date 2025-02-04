#Link: https://leetcode.com/problems/rearrange-string-k-distance-apart/
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        count = Counter(s)
        maxHeap = [ (-f, c) for c, f in count.items()]
        heapq.heapify(maxHeap)
        res = ""

        while maxHeap:
            temp = {}
            if maxHeap[0][0] == -1:
                d = len(maxHeap)
            else:
                d = k
            for _ in range(d):
                if maxHeap:
                    f, c = heapq.heappop(maxHeap)
                    res += c
                    temp[c] = -f
                else:
                    return ""
            
            for c, f in temp.items():
                if f - 1 > 0:
                    heapq.heappush(maxHeap, (-(f-1), c))
        return res