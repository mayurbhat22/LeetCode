#Link: https://leetcode.com/problems/single-threaded-cpu/
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        res = []
        minHeap = []

        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x:x[0])
        i, t = 0, tasks[0][0]
        while minHeap or i < n:
            while i < n and tasks[i][0] <= t:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not minHeap:
                t = tasks[i][0]
            else:
                processingTime, index = heapq.heappop(minHeap)
                res.append(index)
                t += processingTime

        return res