#Link: https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            else:
                visited[node] = False #To detect Cycle
            
            is_destination_node = True if node == destination else False

            for nei in adj_list[node]:
                destination_node = dfs(nei)
                if destination_node == False:
                    return False
                else:
                    is_destination_node = destination_node
    
            visited[node] = True
            return is_destination_node
            
        return dfs(source)

"""
Do a DFS from source node.
In order to detect a cycle, make the visited[node] = False.
And in each dfs call, have a is_destination_node = False, because not all nodes end as a destination node.

So, if node is already visitedm return False.
And inside the iteration if a False is returned, no need to go further, return False.
After visiting all of its children, visited[node] = True. Now it is truly explored.
Return is_destination_node, which will carry True if this path has reached till destination.
"""