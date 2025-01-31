#Link: https://leetcode.com/problems/construct-string-with-repeat-limit/
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = ""
        n = repeatLimit
        count = Counter(s)
        maxHeap = []
        for char, count in count.items():
            heapq.heappush(maxHeap, (-ord(char), char, count))
        
        while maxHeap:
            _, char, count = heapq.heappop(maxHeap)
            use = min(count, repeatLimit)
            for _ in range(use):
                res += char
            
            if count > use and maxHeap:
                _, char2, count2 = heapq.heappop(maxHeap)
                res += char2
                count2 -= 1
                heapq.heappush(maxHeap, (-ord(char), char, count - use))
                if count2:
                    heapq.heappush(maxHeap, (-ord(char2), char2, count2))
            
        return res
