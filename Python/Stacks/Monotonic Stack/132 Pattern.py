#Link: https://leetcode.com/problems/132-pattern/
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        previousMinimum = [0] * n
        min_index, min_value = 0, nums[0]

        for i, num in enumerate(nums):
            if num < min_value:
                previousMinimum[i] = i
                min_value = num
                min_index = i
            else:
                previousMinimum[i] = min_index

        stack = []
        for i, num in enumerate(nums):
            while stack and num >= nums[stack[-1]]:
                stack.pop()
            
            if len(stack):
                if nums[i] > nums[previousMinimum[stack[-1]]]:
                    return True
            stack.append(i)

        return False
