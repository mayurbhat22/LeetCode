#Link: https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if char == ")":
                    if not (stack and stack[-1] == "("):
                        return False 
                    else:
                        stack.pop(-1)
                if char == "]":
                    if not (stack and stack[-1] == "["):
                        return False 
                    else:
                        stack.pop(-1)
                if char == "}":
                    if not (stack and stack[-1] == "{"):
                        return False 
                    else:
                        stack.pop(-1)
        return True if len(stack) == 0 else False