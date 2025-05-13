#Link: https://leetcode.com/problems/detonate-the-maximum-bombs/
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adjList = defaultdict(list)
        max_count = 0
        for i in range(n):
            for j in range(n):
                r = bombs[i][2]
                if i!= j:
                    d = sqrt((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2)

                    if d <= r: 
                        adjList[i].append(j)

        def dfs(node):
            nonlocal count
            visited.add(node)
            count += 1
            if node in adjList:
                for nei in adjList[node]:
                    if nei not in visited:
                        dfs(nei)
        
        for i in range(n):
            visited = set()
            count = 0
            dfs(i)
            max_count = max(count, max_count)
        return max_count
    
"""
Since if one bomb explodes, and if another bomb is in the radius it will explode as well and so on.
It is a DFS problem where one bomb will explode another one recursively. 
The main thing is to convert the bomb with Manhattan distance withing radius of a particular bomb to add to the adjList. 
Iterate over each bomb, and calculate the number of bombs that it can implode. Calculate the max count.
"""