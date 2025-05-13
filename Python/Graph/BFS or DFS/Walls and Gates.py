#Link: https://leetcode.com/problems/walls-and-gates/
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        q = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
        while q:
            r, c, dist = q.pop(0)

            for nei in neighbours:
                nr, nc = r + nei[0], c + nei[1]
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2147483647:
                    q.append((nr, nc, dist+1))
                    rooms[nr][nc] = dist + 1
        
"""
Normal BFS.
Reverse Engineering, instead of performing BFS from each empty cell to the nearest gate, perform BFS from the gates.
Put all the cell that has gate into the Queue. Dist would be dist + 1 for each cell. 
BFS would make sure that each cell is at the minium distance since it explores level by level.
"""