#Link: https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()

                repeat = ""
                while stack and stack[-1].isnumeric():
                    repeat = stack.pop() + repeat
                
                string = string * int(repeat)
                stack.append(string)
            else:
                stack.append(char)
        return "".join(stack)

