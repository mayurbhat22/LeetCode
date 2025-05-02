#Link: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        state = (grid[0][0], 0, 0)
        pq = [(state)]
        costs = [[float('inf')] * n for _ in range(m)]
        costs[0][0] = grid[0][0]
        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
   
        while pq:
            obstacles, r, c = heapq.heappop(pq)

            if r == m - 1 and c == n - 1:
                return obstacles

            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n:
                    temp = obstacles + grid[nr][nc]
                    if temp < costs[nr][nc]:
                        new_state = (temp, nr, nc)
                        heapq.heappush(pq, new_state)
                        costs[nr][nc] = temp
        
        return costs[m-1][n-1]
    
"""
Dijktra’s Algorithm on Matrix. (BFS)
For each cell, calculate the minimum obstacles removed to reach the cell.
If the new obstacle is less, replace the old value.
Priority Queue will be used to get the minium cell at each level.
"""