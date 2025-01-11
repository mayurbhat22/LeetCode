#Link: https://leetcode.com/problems/remove-covered-intervals/
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start_pos = intervals[0][0]
        end_pos = intervals[0][1]
        count = len(intervals)

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if start_pos <= interval[0] and interval[1] <= end_pos:
                count -= 1
            elif start_pos >= interval[0] and interval[1] >= end_pos:
                count -= 1
                start_pos = interval[0]
                end_pos = interval[1]
            else:
                start_pos = interval[0]
                end_pos = interval[1]
        return count