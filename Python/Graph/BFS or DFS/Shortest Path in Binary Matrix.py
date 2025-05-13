#Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        queue = []
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        dist = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                if r == n - 1 and c == n - 1:
                    return dist
                
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr <= n-1 and 0 <= nc <= n-1 and grid[nr][nc] == 0 and (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            dist += 1
        
        return -1

"""
When you see "Shortest" in a question, BFS is typically the best approach.
Since BFS explores level by level, reaching the last cell will give us the minimum path length.
"""