#Link: https://leetcode.com/problems/parallel-courses/
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        indegree = [0] * (n+1)

        for u, v in relations:
            adj_list[u].append(v)
            indegree[v] += 1
        
        q = deque()
        semester = 0
        for node in range(1,n+1):
            if indegree[node] == 0:
                q.append(node)
        
        count = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                count += 1
                for nei in adj_list[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            semester += 1
        
        return semester if count == n else -1

"""
So, if the indegree[course] == 0, that means we have to start with those courses in the first semeseter.
Add it to the queue.
Now, calculate the level to which the BFS will go, and that will be the minimum number of semesters.

In each BFS call,
Check for the adjacency course, and reduce its indegree by 1. Meaning the current course is taken, and if the indegree is 0, that means all of its prerequisite is done, and that course can be taken next. Add it to the queue.
Do a level order traversal.
"""