#Link: https://leetcode.com/problems/shortest-path-to-get-food/
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        visited = set()

        # Worst Case - O(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    q.append((i, j, 0))
                    visited.add((i, j))
                    break
        

        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        # O(m*n)
        while q:
            r, c, dist = q.pop(0)

            if grid[r][c] == "#":
                return dist

            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited and grid[nr][nc] != "X":
                    q.append((nr, nc, dist+1))
                    visited.add((nr, nc))
        
        return -1