from collections import defaultdict
from sortedcontainers import SortedList


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)

        # Step 1: Build components using DSU
        for u, v in connections:
            dsu.union(u, v)
        
        # Step 2: Group nodes by component root
        comps = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            comps[root].append(i)
        
        # Step 3: Build online sets for each component
        online = {}
        for root, nodes in comps.items():
            online[root] = SortedList(nodes)
        
        is_online = [True] * (c + 1)
        res = []

        # Step 4: Process queries
        for typ, x in queries:
            root = dsu.find(x)
            
            if typ == 1:  # maintenance check
                if is_online[x]:
                    res.append(x)
                else:
                    if online[root]:
                        res.append(online[root][0])  # smallest ID
                    else:
                        res.append(-1)
            
            elif typ == 2:  # take station offline
                if is_online[x]:
                    is_online[x] = False
                    if root in online:
                        online[root].discard(x)  # remove efficiently
        return res
        