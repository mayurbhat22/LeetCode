#Link: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
#BFS:
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj_list = defaultdict(list)
        indegree = [0] * (len(roads)+1)
        children = [0] * (len(roads)+1)
        for u, v in roads:
            adj_list[u].append(v)
            adj_list[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        min_fuel = 0
        q = deque()
        visited = set()
        for node in range(len(roads)+1):
            if indegree[node] == 1 and node != 0:
                q.append(node)

        while q:
            node = q.popleft()
            visited.add(node)
            min_fuel += ceil((children[node]+1)/seats)
            
            for parent in adj_list[node]:
                if parent not in visited:
                    indegree[parent] -= 1
                    children[parent] += children[node] + 1
                    if indegree[parent] == 1 and parent != 0:
                        q.append(parent)
        
        return min_fuel

#DFS
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj_list = defaultdict(list)
        for u, v in roads:
            adj_list[u].append(v)
            adj_list[v].append(u)

        min_fuel = 0
        visited = set()

        def dfs(node):
            nonlocal min_fuel
            visited.add(node)

            children = 0
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    children += dfs(nei)
            total_nodes = children + 1
            if node != 0:
                min_fuel += ceil(total_nodes/seats)
            return total_nodes

        dfs(0)
        
        return min_fuel

"""
DFS Approach:
For each node, we want to number of children nodes, so that we can calcualte how many fuel it is going to cost to go to the parent node.

So, start a DFS from 0, and for each node, after calculating the number of children, the fuel cost will be ceil(children+1/seats).

BFS Approach:
We have to start the BFS approach from the nodes where indegree is just 1, since these are bi-directional edges.

Start a Multisource BFS from all the nodes that have indegree = 1.
In each calculation, indegree[parent] -= 1. And if the indegree[parent] == 1, that means all children are calculated, add it to the queue.
Also, need to maintain, children[] array to calculate the number of children.
When a node is popped, calculate the fuel as ceil(children[node]+1/seats).
"""