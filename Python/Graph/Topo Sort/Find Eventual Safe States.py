#Link: https://leetcode.com/problems/find-eventual-safe-states/
#Topo Sort Approach
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj_list = defaultdict(list)
        for i in range(n):
            edges = graph[i]
            for e in edges:
                adj_list[e].append(i)
                indegree[i] += 1

        q = deque()
        answer = []
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
                answer.append(node)

        while q:
            node = q.popleft()
            
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    answer.append(nei)
        
        return sorted(answer)

#DFS Approach
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj_list = defaultdict(list)
        for i in range(n):
            edges = graph[i]
            for e in edges:
                adj_list[i].append(e)

        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            else:
                visited[node] = False
            
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
            
            visited[node] = True
            return True

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res
