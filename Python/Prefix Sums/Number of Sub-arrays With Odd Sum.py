#Link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        hash_map = {0:0, 1:0}
        res = 0
        curr_sum = 0

        for num in arr:
            curr_sum += num
            if curr_sum % 2 == 0:
                res += hash_map[1]
                hash_map[0] += 1
            else:
                res += 1
                res += hash_map[0]
                hash_map[1] += 1

        return res % ((10 ** 9) + 7)