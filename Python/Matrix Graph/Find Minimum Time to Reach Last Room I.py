#Link: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        time = [[float("inf")] * m for _ in range(n)]
        pq = [(0, 0, 0)]
        neibhours = [[1,0], [0,1], [-1,0], [0,-1]]

        while pq:
            t, r, c = heapq.heappop(pq)

            if r == n-1 and c == m-1:
                return t

            for nei in neibhours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < n and 0 <= nc < m:
                    wait_time = max(moveTime[nr][nc]  - t, 0)
                    new_time = t + 1 + wait_time
                    if new_time < time[nr][nc]:
                        time[nr][nc] = new_time
                        heapq.heappush(pq, (new_time, nr, nc))
        
        return 0

"""
Perform Dijktra’s BFS.
To reach each cell, there are 2 options.
1) If the cell he has reached timing is greater than the next cell’s time, that means he is early.
Then to reach the next cell, he can do that just by reaching that cell in t + 1 minutes.
2) If the cell he reached, for example at 4th minute, and if he can reach the next cell only at 7th minute, then he has to wait 3 seconds before moving.
Therefore the time is to reach the next cell is 
max(next cell - t, 0) + 1

And if the time is less than the current cells timings(Dijktra’s), then replace it.
The time you reach the last cell will be the shortest time.
"""