#Link: https://leetcode.com/problems/find-longest-awesome-substring/
class Solution:
    def longestAwesome(self, s: str) -> int:
        mp = {0:-1}
        max_len = 0
        curr_xor = 0
        for i in range(len(s)):
            ch = s[i]
            shift = 1 << ord(ch) - ord('0')
            curr_xor ^= shift

            if curr_xor in mp:
                max_len = max(max_len, i - mp[curr_xor])
            
            for ch1 in range(ord('0'), ord('9')+1):
                shift = 1 << ch1 - ord('0')

                check_xor = curr_xor ^ shift
                if check_xor in mp:
                    max_len = max(max_len, i - mp[check_xor])
            mp[curr_xor] = min(mp[curr_xor], i) if curr_xor in mp else i
        return max_len