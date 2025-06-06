#Link: https://leetcode.com/problems/string-without-aaa-or-bbb/
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res, maxHeap = "", []
        for count, char in [(-a, "a"), (-b, "b")]:
            heapq.heappush(maxHeap, (count, char))
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                else:
                    count2, char2 = heapq.heappop(maxHeap)
                    res += char2
                    count2 += 1
                    if count2:
                        heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))
        return res