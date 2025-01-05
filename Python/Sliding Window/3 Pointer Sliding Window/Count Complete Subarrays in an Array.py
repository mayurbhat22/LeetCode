#Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l_far, l_close, r = 0, 0, 0
        count_map = Counter(nums)
        hash_map = {}
        count = 0
        n = len(count_map)
        ans = 0

        for r in range(len(nums)):
            num = nums[r]
            hash_map[num] = hash_map.get(num, 0) + 1
            if hash_map[num] == 1:
                count += 1
            
            if count == n:
                while hash_map[nums[l_close]] != 1:
                    hash_map[nums[l_close]] -= 1
                    l_close += 1
                ans += (l_close - l_far + 1)

            while count > n:
                hash_map[nums[l_close]] -= 1
                l_close += 1
                l_far = l_close
            
        return ans

