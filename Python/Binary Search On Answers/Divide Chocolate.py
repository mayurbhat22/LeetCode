#Link: https://leetcode.com/problems/divide-chocolate/
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        totalSweetness = sum(sweetness)
        if k == 0:
            return totalSweetness
        low, high = 1, totalSweetness // k
        ans = 0

        def divisionPossible(minSweetness):
            count = 0
            curr_sum = 0
            for s in sweetness:
                if curr_sum + s >= minSweetness:
                    curr_sum = 0
                    count += 1
                else:
                    curr_sum += s
                print(curr_sum, count)
            if curr_sum >= minSweetness:
                count += 1
            return count >= (k+1)

        while low <= high:
            mid = low + (high-low) // 2
            if(divisionPossible(mid)):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans