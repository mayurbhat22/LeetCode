#Link: https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        visited = set()
        number_of_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    number_of_oranges += 1
        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        minute = 0
        while q:
            r, c, minute = q.pop(0)

            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    q.append((nr,nc,minute+1))
                    visited.add((nr,nc))
                    number_of_oranges -= 1
        return minute if number_of_oranges == 0 else -1
    
"""
Iterate over each cell, and if it has a rotten orange, add it to the queue.
Perform BFS starting from all rotten oranges simultaneously. Since visiting a neighboring cell takes 1 minute, adjacent fresh oranges will become rotten at t + 1 minutes.
Using BFS ensures each orange becomes rotten in the minimum possible time since we explore level by level.
Return the total minutes if all oranges become rotten, or -1 if any fresh oranges remain.
"""