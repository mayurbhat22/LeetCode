class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        shortest_distance = [0] * n
        for i in range(n-1):
            adj_list[i].append(i+1)
            shortest_distance[i+1] = i+1
        
        def bfs(node):
            q = deque([(node, shortest_distance[node])])
            
            while q:
                node, dist = q.popleft()
 
                for nei in adj_list[node]:
                    if dist + 1 <= shortest_distance[nei]:
                        shortest_distance[nei] = dist + 1
                        q.append((nei, dist + 1))
            return shortest_distance[n-1]

        answer = []
        min_dist = float("inf")
        for q in queries:
            adj_list[q[0]].append(q[1])
            node = q[0]
            if q[0] < q[1]:
                node = q[0]
            answer.append(min(min_dist, bfs(node)))
        
        return answer

"""
In the beginning, distance from 0 to each node will be the node itself.
So, shortest_distance[i] means the distance at which node i is from 0.
So, for each query, add the edge into adjaceny list, and do a BFS from 0.
While doing BFS, the since the adj_list has changed, the shortest_distance will hold the shortest distance.

In order to save time, we can do a BFS from the edge u, in u → v instead of 0. Since only that edge is changed for that particular query.
"""