#Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        distance_from_node_1 = [float("inf")] * n
        distance_from_node_2 = [float("inf")] * n

        distance_from_node_1[node1] = 0
        distance_from_node_2[node2] = 0

        def bfs(starting_node, distance):
            q = deque([(starting_node, 0)])
            while q:
                node, dist = q.popleft()

                if edges[node] != -1:
                    nei = edges[node]
                    if dist + 1 < distance[nei]:
                        q.append((nei, dist + 1))
                        distance[nei] = dist + 1

        bfs(node1, distance_from_node_1)
        bfs(node2, distance_from_node_2)
        
        min_dist = float("inf")
        min_index = float("inf")
        for node in range(n):
            dist_1 = distance_from_node_1[node]
            dist_2 = distance_from_node_2[node]
            if dist_1 != float("inf") and dist_2 != float("inf"):
                if max(dist_1, dist_2) < min_dist:
                    min_dist = max(dist_1, dist_2)
                    min_index = node
        
        return min_index if min_index != float("inf") else -1
    
"""
First, calculate the distance of each node from the node1 and node2 seperately, by doing BFS.

Then, iterate over each node, and check if the node is reachable from both the nodes.
If the node is reachable, then the max distance between node1 and node, and node2 and node should be minimum.
So if it less than the already calculated min_distance, replace it.
"""