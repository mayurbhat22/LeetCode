#Link: https://leetcode.com/problems/count-vowel-strings-in-ranges/
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        hash_map = {-1 : 0}
        res = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        running_sum = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                running_sum += 1
            hash_map[i] = running_sum
        # print(hash_map)
        for q in queries:
            res.append(hash_map[q[1]] - hash_map[q[0]-1])
        return res
