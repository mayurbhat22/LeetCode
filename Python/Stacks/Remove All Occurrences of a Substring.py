#Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for char in s:
            stack.append(char)
            j = len(part) - 1
            i = len(stack) - 1
            while i >= 0 and j >= 0 and stack[i] == part[j]:
                i -= 1
                j -= 1
            if j < 0:
                count = 0
                while stack and count < len(part):
                    stack.pop()
                    count += 1
        return "".join(stack)