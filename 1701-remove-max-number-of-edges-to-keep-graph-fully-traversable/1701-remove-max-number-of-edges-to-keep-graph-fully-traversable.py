class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        puf = UnionFind(n)
        tuf = UnionFind(n)
        res = 0
        for edge in edges:
            if edge[0] == 3:
                if puf.union(edge[1], edge[2]) == 1:
                    tuf.union(edge[1], edge[2])
                    res += 1
            if puf.is_connected() and tuf.is_connected():
                return len(edges) - res
        for edge in edges:
            if edge[0] == 1:
                res += puf.union(edge[1], edge[2])
            if edge[0] == 2:
                res += tuf.union(edge[1], edge[2])
            if puf.is_connected() and tuf.is_connected():
                return len(edges) - res
        return -1

class UnionFind:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        self.node_count = n
    def find(self, x):
        if self.parent[x] == 0 or self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 0
        self.parent[py] = px
        self.node_count -= 1
        return 1
    def is_connected(self):
        return self.node_count == 1