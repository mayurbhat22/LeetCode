#Link: https://leetcode.com/problems/network-delay-time/
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for i in range(n+1)]

        for u, v, w in times:
            adjList[u].append((v, w))
        
        time = [float("inf")] * (n+1)
        pq = [(0, k)]
        time[k] = 0

        while pq:
            t, node = heapq.heappop(pq)

            for nei, w in adjList[node]:
                if t + w < time[nei]:
                    time[nei] = t + w
                    heapq.heappush(pq, (t + w, nei))

        min_time = max(time[1:])   
        return min_time if min_time != float("inf") else -1
    
"""
Normal BFS, or Dijktras would work.
Find the shortest time it will take to reac each node from the source, (k).
Then the max time among that will be the answer.
"""