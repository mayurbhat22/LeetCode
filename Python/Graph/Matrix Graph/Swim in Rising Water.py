#Link: https://leetcode.com/problems/swim-in-rising-water/
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        pq = [(grid[0][0], 0, 0)]
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while pq:
            t, r, c = heapq.heappop(pq)
            if r == n-1 and c == n-1:
                return t
            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_time = max(grid[nr][nc], t)
                    heapq.heappush(pq, (new_time, nr, nc))
        
        return times[n-1][n-1]

"""
Use Dijktra’s algorithm.

So at each cell, the time to reach the adjacent cells have 2 options.
1) If the adjacent cells have more time, the it would nei_t - curr_t.

2) If it is lower, then just use the current time.
"""