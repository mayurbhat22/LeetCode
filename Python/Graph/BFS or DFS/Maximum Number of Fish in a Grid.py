#Link: https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        num_of_fish = max_num_of_fish = 0
        def dfs(r, c):
            nonlocal num_of_fish
            num_of_fish += grid[r][c]
            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n and ((nr, nc)) not in visited and grid[nr][nc] > 0:
                    visited.add((nr, nc))
                    dfs(nr ,nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and (i,j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    max_num_of_fish = max(max_num_of_fish, num_of_fish)
                    num_of_fish = 0
        return max_num_of_fish

"""
This problem is similar to "Number of Islands."
Perform a DFS for each island encountered. 
At each cell, add its value to num_of_fish. After completing each DFS traversal, 
update max_num_of_fish with the highest value found.
"""