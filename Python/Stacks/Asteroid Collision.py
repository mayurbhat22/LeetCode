#Link: https://leetcode.com/problems/asteroid-collision/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            poppedValue = 0
            while stack and abs(asteroid) >= abs(stack[-1]) and (asteroid < 0 and stack[-1] > 0):
                if abs(asteroid) > abs(stack[-1]):
                    poppedValue = stack.pop()
                elif abs(asteroid) == abs(stack[-1]):
                    poppedValue = stack.pop()
                    break
            if not stack or (stack and ((asteroid < 0 and stack[-1] < 0) or (asteroid > 0 and stack[-1] > 0) or(asteroid > 0 and stack[-1] < 0))):
                if poppedValue:
                    if abs(asteroid) != abs(poppedValue):
                        stack.append(asteroid)
                else:
                    stack.append(asteroid)
            
        return stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and (asteroid < 0 and stack[-1] > 0):
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                elif abs(asteroid) < abs(stack[-1]):
                    asteroid = 0
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    asteroid = 0
                    break
            if asteroid:
                stack.append(asteroid)
            
        return stack
