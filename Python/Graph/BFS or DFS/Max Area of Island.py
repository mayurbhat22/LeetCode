#Link: https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        land_area = max_land_area = 0
        def dfs(r, c):
            nonlocal land_area
            land_area += 1
            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n and ((nr, nc)) not in visited and grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    dfs(nr ,nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    max_land_area = max(max_land_area, land_area)
                    land_area = 0
        return max_land_area


"""
Similar to the Number of Islands problem, this solution uses DFS. 
During each DFS traversal of an island, count the number of recursive DFS calls to calculate that island's area. 
Track the maximum area encountered after completing each island's DFS traversal.
"""