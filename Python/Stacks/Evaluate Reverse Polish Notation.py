#Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                first_ele = stack.pop()
                second_ele = stack.pop()
                stack.append(first_ele + second_ele)
            elif char == "-":
                first_ele = stack.pop()
                second_ele = stack.pop()
                stack.append(second_ele - first_ele)
            elif char == "*":
                first_ele = stack.pop()
                second_ele = stack.pop()
                stack.append(first_ele * second_ele)
            elif char == "/":
                first_ele = stack.pop()
                second_ele = stack.pop()
                stack.append(int(second_ele / first_ele))
            else:
                stack.append(int(char))
            # print(stack)
        return stack.pop()