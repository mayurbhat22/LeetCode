#Link: https://leetcode.com/problems/reorganize-string/
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        map = {}
        res = ""
        for char in s:
            map[char] = map.get(char, 0) + 1

        max_heap = []
        for char, count in map.items():
            heapq.heappush(max_heap, (-count, char))
        print(max_heap)
        while len(max_heap)>1:
            current_char = heapq.heappop(max_heap)[1]
            next_char = heapq.heappop(max_heap)[1]
            res = res + current_char + next_char
            map[current_char] = map.get(current_char) - 1
            map[next_char] = map.get(next_char) - 1
            if map.get(current_char) > 0:
                heapq.heappush(max_heap, (-map.get(current_char), current_char))
            if map.get(next_char) > 0:
                heapq.heappush(max_heap, (-map.get(next_char), next_char))
        
        if len(max_heap) > 0:
            char = heapq.heappop(max_heap)[1]
            if map.get(char) > 1:
                return ""
            else:
                res = res + char
        
        return res