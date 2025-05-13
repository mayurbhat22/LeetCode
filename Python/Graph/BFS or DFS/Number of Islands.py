#Link: https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        def dfs(r, c):
            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == "1":
                    visited.add((nr, nc))
                    dfs(nr ,nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    res += 1
        return res

"""
Iterate through each cell and check if it has been visited. If not, start either a BFS or DFS from that cell.

For BFS, create a new queue for each BFS call. Add all adjacent cells to the queue and process them by marking them as visited. When all connected cells are processed, increment the island count.

For DFS, recursively explore adjacent cells and mark them as visited. After completing each DFS call from the main loop, increment the island count.
"""