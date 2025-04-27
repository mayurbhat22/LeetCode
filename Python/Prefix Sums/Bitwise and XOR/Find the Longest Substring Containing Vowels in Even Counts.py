#Link: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_map = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
        mp = {0: -1}
        curr_xor = 0
        max_len = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in vowel_map:      
                shifted_character = 1 << (vowel_map[ch] - 1)
                curr_xor ^= shifted_character

            if curr_xor in mp:
                max_len = max(max_len, i - mp[curr_xor])
            else:
                mp[curr_xor] = i
 
        return max_len
            