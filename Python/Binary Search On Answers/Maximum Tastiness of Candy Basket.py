#Link: https://leetcode.com/contest/weekly-contest-325/problems/maximum-tastiness-of-candy-basket/
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        low, high = 0, max(price)
        ans = 0
        price.sort()
        
        def tastinessPossible(minAbsDiff):
            count = 1
            prevPrice = price[0]
            for i in range(1, len(price)):
                if price[i] - prevPrice >= minAbsDiff:
                    count += 1
                    prevPrice = price[i]

            return count >= k
            
        while low <= high:
            mid = low + (high - low) // 2
            if(tastinessPossible(mid)):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans