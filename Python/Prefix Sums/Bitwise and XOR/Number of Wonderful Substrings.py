#Link: https://leetcode.com/problems/number-of-wonderful-substrings/
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mp = {0: 1}
        res = 0
        curr_xor = 0
        for ch in word:
            shift = ord(ch) - ord('a')
            shift = 1 << shift
            curr_xor = curr_xor ^ shift

            if curr_xor in mp:
                res += mp[curr_xor]
            
            for ch1 in ['a','b','c','d','e','f','g','h','i','j']:
                shift = ord(ch1) - ord('a')
                check_xor = curr_xor ^ (1 << shift)

                if check_xor in mp:
                    res += mp[check_xor]
            mp[curr_xor] = mp.get(curr_xor, 0) + 1
        return res