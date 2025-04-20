#Link: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        state = (0, 0, 0)
        q = [(0, state)]
        visited = set([state])

        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        
        # O(m*n)
        while q:
            dist, (r, c, obstacles) = q.pop(0)

            if r == m-1 and c == n-1:
                return dist

            for nei in neighbours:
                temp = obstacles
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n:
                    temp += grid[nr][nc]
                    new_state = (nr, nc, temp)
                    if new_state not in visited and temp <= k:
                        q.append((dist+1, new_state))
                        visited.add(new_state)
        
        return -1

"""
Normal BFS on graph, with additional requierements.

Start from the cell (0, 0).
Neighbours will be adjacent cells, excluding diagonal.

Need to store the state for each cell.
To reach a cell, there are multiple paths.
If we have to reach the Cell (2,3), there is the path followed by green arrow, and one followed by yellow arrow. We reach, with exact same distance, but since the green arrow path never used a obstacle, that would be a new state.
(2, 3, 0) 0 → Meaning 0 obstacles were used.

So, at each level, check if the obstacles is exhausted.
If exhausted we cannot continue.

Since the problem is asking to reach the end cell, whenever we reach, return the distance.
"""