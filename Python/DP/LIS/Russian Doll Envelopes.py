#Link: https://leetcode.com/problems/russian-doll-envelopes/
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        temp = [envelopes[0][1]]
        res = 1
        for i in range(1, n):
            if temp[-1] < envelopes[i][1]:
                temp.append(envelopes[i][1])
                res += 1
            else:
                index = bisect_left(temp, envelopes[i][1])
                temp[index] = envelopes[i][1]
        
        return res