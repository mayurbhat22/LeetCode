#Link: https://leetcode.com/problems/task-scheduler/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        res = 0
        length = n
        maxHeap = []

        for c, f in count.items():
            heapq.heappush(maxHeap, (-f, c))

        while maxHeap:
            temp = {}
            n = length + 1
            for _ in range(n):
                if maxHeap:
                    ele = heapq.heappop(maxHeap)
                    f, c = -ele[0], ele[1]
                    temp[c] = f
            print(maxHeap, temp, n)
            for c, f in temp.items():
                if f - 1  > 0:
                    heapq.heappush(maxHeap, (-(f-1), c))
            print(maxHeap)
            res += len(temp) if not maxHeap else n

        return res