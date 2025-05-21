#Link: https://leetcode.com/problems/reachable-nodes-with-restrictions/
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj_list = defaultdict(list)
        visited = set(restricted)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        q = deque([0])
        visited.add(0)
        res = 1
        while q:
            node = q.popleft()

            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
                    res += 1
        return res
    
"""
Normal BFS, where we count number of nodes visited.
Once you encounter restricted node, you cannot go further in that path, meaning do not add it the queue to explore.
To make it more conveninet, just add the restricted nodes to visited set in the beginning.
"""