#Link: https://leetcode.com/problems/shortest-path-with-alternating-colors/
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u, v in redEdges:
            adj_list[u].append((v, 0))
        for u, v in blueEdges:
            adj_list[u].append((v, 1))
        answer = [-1] * n

        #BFS
        q = deque([(0, 0, -1)])
        visited = [[False]*2 for _ in range(n)]
        visited[0][1] = visited[0][0] = True
        while q:
            node, dist, colour = q.popleft()

            if answer[node] == -1 or (answer[node] != -1 and answer[node] > dist):
                answer[node] = dist

            for nei, edj_colour in adj_list[node]:
                if not visited[nei][edj_colour] and colour != edj_colour:
                    q.append((nei, dist+1, edj_colour))
                    visited[nei][edj_colour] = True
        
        return answer

"""
Since the problem is askng “Shortest”, BFS is used.
Create a Adjacency list for red_edges Marking the edge as 0 and blue_edges marking the edge as 1.

Main mistake made earlier, visited cannot be just a set.
Because, a node once visited by traversing red edge, and for the next time can be visited using blue edge if it is there.
So a visited should be visited[n][2]. 
Traverse through the nodes and its edges, if the dej_color is different than the current color, add the node to the queue and mark it as visited[nei][edj_color].
And when the node is popped, if the dist < answer[node], answer[node] = dist.
"""