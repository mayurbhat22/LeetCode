#Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {}
        curr_sum, max_sum, left = 0, 0, 0
        repeated_count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            hash_map[nums[right]] = hash_map.get(nums[right], 0) + 1
            if hash_map[nums[right]] == 2:
                repeated_count += 1
            
            if right - left + 1 == k:
                if repeated_count == 0:
                    max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[left]
                hash_map[nums[left]] -= 1
                if hash_map[nums[left]] == 1:
                    repeated_count -= 1
                left += 1
        return max_sum
    

#Solution-2
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {}
        curr_sum, max_sum, left = 0, 0, 0
        count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            hash_map[nums[right]] = hash_map.get(nums[right], 0) + 1
            if hash_map[nums[right]] == 1:
                count += 1
            
            if right - left + 1 == k:
                if count == k:
                    max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[left]
                hash_map[nums[left]] -= 1
                if hash_map[nums[left]] == 0:
                    count -= 1
                left += 1
        return max_sum