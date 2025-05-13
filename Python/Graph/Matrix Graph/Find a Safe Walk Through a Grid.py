#Link: https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        state = ( -health + grid[0][0], 0, 0)
        pq = ([state])
        healths = [[float("-inf")] * n for _ in range(m)]
        healths[0][0] = -health + grid[0][0]
        neigbhours = [[1,0], [0,1], [-1,0], [0,-1]]
        while pq:
            h, r, c = heapq.heappop(pq)
            h = -h
            if r == m-1 and c == n-1 and h >= 1:
                return True

            for nei in neigbhours:
                nr, nc = r + nei[0], c + nei[1]

                if 0 <= nr < m and 0 <= nc < n:
                    new_health = h - grid[nr][nc]
                    new_state = (-new_health, nr, nc)
                    if new_health >= 1 and new_health > healths[nr][nc]:
                        heapq.heappush(pq, new_state)
                        healths[nr][nc] = new_health

        return False
    
"""
You can use either normal BFS or BFS with Dijkstra's algorithm.

Normal BFS:
You need to find a way to reach a cell with maximum health. For each cell, maintain a state (health, i, j) that tracks the health level when reaching that cell. If the health is higher, use that state. Health decreases when encountering a 1 in the cell. Continue adding the current state to the queue only if health is ≥ 1.

BFS with Dijkstra's:
The procedure remains the same, but we need a max heap since we need to find maximum health at each cell. Only update the cell if the current health is greater than the cell's health.

If at any time we can reach the last cell with health ≥ 1, we can return True.
"""