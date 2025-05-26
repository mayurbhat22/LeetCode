#Link: https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 1_000_000_000
        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))

        distanceToLastNode = [float("inf")] * (n+1)
        distanceToLastNode[n] = 0
        pq = [(0, n)]

        while pq:
            dist, node = heapq.heappop(pq)

            for nei, edj_wt in adj_list[node]:
                if dist + edj_wt < distanceToLastNode[nei]:
                    distanceToLastNode[nei] = dist + edj_wt
                    heapq.heappush(pq, (dist + edj_wt, nei))
        
        def dfs(node, curr_dist):
            if node == n:
                return 1
            
            if dp[node] != -1:
                return dp[node]
            total_path = 0
            for nei, edj_wt in adj_list[node]:
                if curr_dist > distanceToLastNode[nei]:
                    total_path += dfs(nei, distanceToLastNode[nei])
            dp[node] = total_path % (MOD + 7)
            return dp[node]
        
        dp = [-1] * (n+1)
        return dfs(1, distanceToLastNode[1]) % (MOD + 7)

"""
First, calculate the distance of each node from the lat node.
Now start a DFS cal from the node 0.
If the curr_distance > adj_node’s distance, continue with the DFS call.
And since there might be many sub calls from the same node, cache it using a dp array.
"""