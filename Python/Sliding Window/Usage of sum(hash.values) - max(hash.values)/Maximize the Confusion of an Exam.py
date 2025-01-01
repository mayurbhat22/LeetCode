#Link: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left, ans, max_val = 0, 0, 0
        char_map = {}
        for right in range(len(answerKey)):
            char_map[answerKey[right]] = char_map.get(answerKey[right], 0) + 1

            curr_sum = right - left + 1
            max_val = max(max_val, char_map[answerKey[right]])
            while left<=right and curr_sum - max_val > k:
                char_map[answerKey[left]] = char_map.get(answerKey[left], 0) - 1
                curr_sum -= 1
                left += 1

            ans = max(ans, right - left + 1)
        
        return ans