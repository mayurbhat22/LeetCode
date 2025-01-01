class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            map[char] = map.get(char, 0) + 1

            while l < r and sum(map.values()) - max(map.values()) > k:
                map[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len