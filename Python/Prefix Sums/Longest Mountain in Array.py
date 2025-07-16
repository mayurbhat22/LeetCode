#Link: https://leetcode.com/problems/longest-mountain-in-array
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_increasing = [1] * n
        prefix_decreasing = [1] * n

        prev_hei = arr[0]
        for i in range(1, n):
            hei = arr[i]
            if hei > prev_hei:
                prefix_increasing[i] += prefix_increasing[i-1] 
            prev_hei = hei
        
        prev_hei = arr[n-1]
        for i in range(n-1, -1, -1):
            hei = arr[i]
            if hei > prev_hei:
                prefix_decreasing[i] += prefix_decreasing[i+1] 
            prev_hei = hei
        
        max_height = 0
        for i in range(1, n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                max_height = max(max_height, prefix_increasing[i] + prefix_decreasing[i] - 1)
        
        return max_height

