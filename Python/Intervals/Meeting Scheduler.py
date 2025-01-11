#Link: https://leetcode.com/problems/meeting-scheduler/
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        s1 = s2 = 0
        ans = []

        while s1 < len(slots1) and s2 < len(slots2):
            if (slots1[s1][1] >= slots2[s2][0] and slots2[s2][1] >= slots1[s1][0]) or (slots2[s2][1] >= slots1[s1][0] and slots1[s1][1] >= slots2[s2][0]):
                intersectEnd = min(slots1[s1][1], slots2[s2][1])
                intersectStart = max(slots1[s1][0], slots2[s2][0])
                if intersectEnd - intersectStart >= duration:
                    return [intersectStart, intersectStart + duration]
            if slots1[s1][1] > slots2[s2][1]:
                s2 += 1
            else:
                s1 += 1
        return ans 
