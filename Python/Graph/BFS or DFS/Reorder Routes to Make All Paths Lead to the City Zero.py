#Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
#DFS Approach
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        adjList = defaultdict(list)
        changes = 0
        visited = set()

        for a, b in connections:
            adjList[a].append((b,1))
            adjList[b].append((a,0))
        
        def dfs(city):
            nonlocal changes
        
            for nei in adjList[city]:
                if nei in visited:
                    continue
                if (nei, city) not in edges:
                    changes += 1
                dfs(nei)
        
        visited.add(0)
        dfs(0)

#BFS Approach
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        adjList = defaultdict(list)
        changes = 0
        visited = set()

        for a, b in connections:
            adjList[a].append((b,1))
            adjList[b].append((a,0))
        
        q = deque([0])
        visited.add(0)
        while q:
            city = q.popleft()

            for nei, edj_direction in adjList[city]:
                if nei in visited:
                    continue
                changes += edj_direction
                q.append(nei)
                visited.add(nei)


        return changes

"""
Create an Adjaceny list, along with the directed edges as set.
The intuition is, if all the edges should be directed to 0, then the nodes connected to 0, should have all the edges pointing from that node to 0.
And then its children should have the edges pointing towards parent and so on…

DFS/BFS Approach.

Start a DFS from 0.
For each of its children, calculate if the edge (children, present_node) is in the edge_set.
meaning if there is already a edge pointing towards the parent. If not, changes += 1.
Then do a DFS(children).

Another approach:
Store 1 if there from u → v. For edge v → u, store 0.
so, changes would be changes += edj_direction, meaning if the edj_direction = 1, then it has to be reversd since it is a edge from parent → child and not child → parent.
"""