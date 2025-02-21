#Link: https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        h = ans = w = 0

        for i, heig in enumerate(height):
            while stack and heig >= height[stack[-1]]:
                top = stack.pop()
                if len(stack):
                    h = min(heig, height[stack[-1]]) - height[top]
                    w = i - (stack[-1] + 1)
                    ans += h * w
            stack.append(i)
        return ans
