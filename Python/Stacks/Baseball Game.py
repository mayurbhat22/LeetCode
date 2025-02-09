#Link: https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == "C":
                if stack:
                    stack.pop(-1)
            elif o == "D":
                if stack:
                    stack.append(2 * stack[-1])
            elif o == "+":
                if len(stack) > 1:
                    stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(o))
        return sum(stack)