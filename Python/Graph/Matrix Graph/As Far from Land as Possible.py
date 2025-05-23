#Link: https://leetcode.com/problems/as-far-from-land-as-possible/
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        neigbhours = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        visited = set()
        q = deque([])
        dist = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))

        while q:
            r, c, dist = q.popleft()

            for nei in neigbhours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] != 1:
                    q.append((nr, nc, dist+1))
                    visited.add((nr, nc))
            
        return dist if dist != 0 else -1
    
"""
Start a Multisource BFS from all the cells that has 1 in it.
Calculate the distance of all the 0’s.
This will make all the 0’s to have the distance of the nearest 1.
Then take the maximum value from this.
"""