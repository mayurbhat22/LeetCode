#Link: https://leetcode.com/problems/xor-queries-of-a-subarray/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        hashMap = {}
        hashMap[-1] = 0
        ans = []
        for i, num in enumerate(arr):
            hashMap[i] = hashMap[i-1] ^ num
        
        for left, right in queries:
            ans.append(hashMap[right] ^ hashMap[left-1])
        return ans