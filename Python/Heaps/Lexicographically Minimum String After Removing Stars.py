#Link: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars
class Solution:
    def clearStars(self, s: str) -> str:
        min_heap = []
        char_set = set()

        for i, char in enumerate(s):
            if char == "*":
                char_value, index = heapq.heappop(min_heap)
                char_set.add(i)
                char_set.add(-index)
            else:
                heapq.heappush(min_heap, (char, -i))

        res = ""
        for i, char in enumerate(s):
            if i not in char_set:
                res += char
        return res