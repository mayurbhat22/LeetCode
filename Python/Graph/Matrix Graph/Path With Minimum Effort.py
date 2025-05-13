#Link: https://leetcode.com/problems/path-with-minimum-effort/
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        effort = [[float("inf")] * m for _ in range(n)]
        pq = [(0, 0, 0)]
        effort[0][0] = 0
        neibhours = [[1,0], [0,1], [-1,0], [0,-1]]

        while pq:
            diff, r, c = heapq.heappop(pq)

            for nei in neibhours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < n and 0 <= nc < m:
                    new_diff = max(abs(heights[r][c] - heights[nr][nc]), diff)
                    if new_diff < effort[nr][nc]:
                        effort[nr][nc] = new_diff
                        heapq.heappush(pq, (new_diff, nr, nc))
        
        return effort[-1][-1]
    
"""
Perform Dijktras with BFS.
At each step, calculate the diff between current cell and the next cell.
Maintain a max diff from the starting point to the end.
Whenever a smaller diff is found compared to the current diff, update it.
Return whatever is saved in [-1][-1], that is last cell.
"""