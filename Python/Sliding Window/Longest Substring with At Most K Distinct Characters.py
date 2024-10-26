class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        map = {}
        max_len = 0

        for r in range(len(s)):
            char = s[r]
            map[char] = map.get(char, 0) + 1
            if map[char] == 1:
                k -= 1
            while k < 0 and l <= r:
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    k += 1
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return max_len