#Link: https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/
class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        edge_set = set()
        for u, v in edges:
            adj_list[u].append((v, 0))
            adj_list[v].append((u, 1))
            edge_set.add((u, v))
        
        answer = [0] * n
        #If the root was 0.
        q = deque([0])
        visited = set()
        visited.add(0)
        number_of_edge_reversal = 0
        while q:
            node = q.popleft()

            for nei, cost in adj_list[node]:
                if nei not in visited:
                    if (node, nei) not in edge_set:
                        number_of_edge_reversal += 1
                    q.append(nei)
                    visited.add(nei)
        
        def dfs(node, parent, curr_cost):
            answer[node] = curr_cost
            for nei, cost in adj_list[node]:
                if nei != parent:
                    if cost == 0:
                        dfs(nei, node, curr_cost + 1)
                    else:
                        dfs(nei, node, curr_cost - 1)

        #If we reroot to every other node.
        dfs(0, -1, number_of_edge_reversal)
        
        return answer

"""
We can do a DFS from each node, and calculate the number of edge reversal changes needs to be there so that it can reach all the nodes.
But this will give TLE.


Optimised approach.
First calculate the number of edge reversal imagining 0 as root.
Edge 2 → 0 needs to be changed in order for node 0 to reach all other nodes.
Now, start a DFS(0,-1,curr_cost), meaning now we will check the edge reversal changes required by imagining each node as route.
So, for each children,
if the cost == 0, that means there is an edge from parent to child, but if we have to make the child as a root, then this edge should be reversed.
So, DFS(child, node, curr_cost + 1).
In the above example, for 0, the child is 2, and the edge is from 2 → 0.
So the cost is 1, and since after rerouting to 2 as root, the edge need not be changed.
So, curr_cost - 1, meaning this edge reversal was in the calculation for changes for 0. Now it has to be subtracted.

For 2, the child is 1, the edge is from 2 → 1.
So, when we reroute the root as 1, the edge 2 → 1 should be changed. So if cost == 0, it is curr_cost + 1.
"""