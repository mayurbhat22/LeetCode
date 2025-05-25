#Link: https://leetcode.com/problems/redundant-connection/
class UnionFind:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [ i for i in range(n+1)]
    
    def find_parent(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    def union(self, node_1, node_2):
        parent_1 = self.find_parent(node_1)
        parent_2 = self.find_parent(node_2)

        if parent_1 == parent_2:
            return False
        if self.rank[parent_1] == self.rank[parent_2]:
            self.parent[parent_2] = parent_1
            self.rank[parent_1] += 1
        elif self.rank[parent_1] < self.rank[parent_2]:
            self.parent[parent_1] = parent_2
        else:
            self.parent[parent_2] = parent_1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        res = []
        for u,v in edges:
            if not uf.union(u, v):
                res.append(u)
                res.append(v)
        
        return res
        

"""
Do Union on all the edges.
When doing Union, if the Ultimate Parent of both the nodes are same, then that is the egde, that has to be returned.
"""