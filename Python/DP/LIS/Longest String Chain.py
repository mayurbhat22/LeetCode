#Link: https://leetcode.com/problems/longest-string-chain/
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x:len(x))
        n = len(words)
        LSC = [1] * n

        def predecessor(word1, word2):
            if len(word1) != len(word2)-1:
                return False
            first = second = 0
            while second < len(word2):
                if first < len(word1) and word1[first] == word2[second]:
                    first += 1
                    second += 1
                else:   
                    second += 1
            if first == len(word1) and second == len(word2):
                return True
            return False

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if predecessor(words[i], words[j]):
                    LSC[i] = max(LSC[i], 1+LSC[j])
        
        return max(LSC)