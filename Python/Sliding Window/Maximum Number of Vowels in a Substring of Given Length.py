#Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        max_count = count = 0

        def isVowel(char):
            return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'
                
        for r in range(len(s)):
            char = s[r]
            count += 1 if isVowel(char) else 0

            if r - l + 1 == k:
                max_count = max(max_count, count)
                count -= 1 if isVowel(s[l]) else 0
                l += 1
        return max_count