#Link: https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        adj_list = defaultdict(list)

        for i, g in enumerate(graph):
            for v in g:
                adj_list[i].append(v)
        
        answer = []
        path = [0]
        def dfs(node):
            if node == n-1:
                answer.append(path[:])
                return

            for nei in adj_list[node]:
                path.append(nei)
                dfs(nei)
                path.remove(nei)
        
        dfs(0)
        return answer

"""
DFS + Backtracking

Start a DFS from 0, have a temp path = [] array where it will store the nodes in the path.
Add each node to the path, then do a DFS, if the node reached is the last node, add the path to the answer array, and return.
After each DFS call, remove the node from the path array, so that other path could also be explored.
"""