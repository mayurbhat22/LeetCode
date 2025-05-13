#Link: https://leetcode.com/problems/find-all-groups-of-farmland/
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        visited = set()
        neighbours = [[0,1],[0,-1],[1,0],[-1,0]]
        ans = []
        def dfs(r, c):
            nonlocal max_val, max_index
            if r+c >= max_val:
                max_val = max(max_val, r+c)
                max_index = (r,c)
            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and land[nr][nc] == 1:
                    visited.add((nr, nc))
                    dfs(nr, nc)

        for i in range(m):
            for j in range(n):
                max_val = float("-inf")
                max_index = (-1, -1)
                if land[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    ans.append([i, j, max_index[0], max_index[1]])
        return ans
"""
For each island, we need to find coordinates r1, c1 and r2, c2.
Each island is rectangular in shape, and no islands are adjacent to each other.
To find islands, iterate through each cell. When encountering a cell with value 1, mark it as the starting point (r1, c1) of an island and begin a DFS from this cell.
To determine r2, c2, maintain a max_index initialized to (-1, -1) and a max_val for each cell.
For each visited cell, if r + c ≥ max_val, update max_val and set max_index to (r, c).
After completing the DFS for an island, add [r1, c1, max_index[0], max_index[1]] to the answer.
"""