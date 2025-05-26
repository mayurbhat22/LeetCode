#Link: https://leetcode.com/problems/path-with-maximum-gold/
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0
        neibhours = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r, c, visited):
            visited.add((r, c))
            max_value = 0
            for nei in neibhours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] > 0:    
                    max_value = max(max_value, dfs(nr, nc, visited))
            visited.remove((r, c))
            return max_value + grid[r][c]

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    visited = set()
                    max_gold = max(max_gold, dfs(i, j, visited))

        return max_gold

"""
DFS + Backtracking

Start from each cell which has gold, i.e, grid[r][c] > 0

In each DFS call, make the cell visited.
Standing at a cell, he can visit up, down, left, right at a time.
So, the return value will be grid[r][c] + max(children).

Why backtracking?

[0,    0,   0]
[0,    0,   2]
[13, 20, 36]
[0,   31, 27]

In this example, you start a DFS from 2,
When you visit cell that contains 36, the options are viist to 20 and 27, and whatever the max will get from children that will be the max value.
But since you already visited the node, it will not visit again.
But the path could be 2→36→27→31→20→13
So, after visiting all of its children, make the visited as False, so that another path could reach there.
"""