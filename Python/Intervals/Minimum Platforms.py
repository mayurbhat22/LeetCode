#Link: https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        a, d = 0, 0
        count = maxCount = 0
        while a < len(arr) and d < len(dep):
            if arr[a] <= dep[d]:
                count += 1
                a += 1
            else:
                count -= 1
                d += 1
            maxCount = max(count, maxCount)
        return maxCount

