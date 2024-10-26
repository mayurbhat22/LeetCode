class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            map[char] = map.get(char, 0) + 1
            while map[char] > 1 and l < r:
                map[s[l]] -= 1
                l += 1
            max_len = max(r - l + 1, max_len)

        return max_len