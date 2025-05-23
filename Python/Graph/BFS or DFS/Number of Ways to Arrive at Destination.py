#Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        adjList = [[] for _ in range(n)]

        for u, v, w in roads:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        
        pq = [(0, 0)]
        times = [[float("inf"), 0]] * n
        times[0] = [0, 1]

        while pq:
            time, node = heapq.heappop(pq)

            for nei, t in adjList[node]:
                if t + time < times[nei][0]:
                    times[nei] = [t + time, times[node][1]]
                    heapq.heappush(pq, (t + time, nei))
                elif t + time == times[nei][0]:
                    times[nei][1] = (times[nei][1] + times[node][1]) % MOD
                
        return times[n-1][1]

"""
Use Dijktra’s algorithm.

We need calculate the time to arrive at destination with minimum amount of time, and also number of ways we can arrive.

So, at first all the time will be inf.
So, if curr_time + nei node time is <, time[] = curr_time + nei_t.
And, the steps would be time[node][1]. That means, since we found new min, the number of ways would be whatever number we had for the current one.

But if the t + time == time[node][0], that means we found more ways to arrive at the same minium time.
Number of ways would be, time[node][1] (Current ways) + time[nei][1] (Already what is there).
"""