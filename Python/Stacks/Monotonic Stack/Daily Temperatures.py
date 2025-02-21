#Link: https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmerTemperature = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                poppedIndex = stack.pop()
                warmerTemperature[poppedIndex] = i - poppedIndex
            
            stack.append(i)
        
        return warmerTemperature