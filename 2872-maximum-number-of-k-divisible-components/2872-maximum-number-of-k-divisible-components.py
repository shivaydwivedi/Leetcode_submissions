from collections import defaultdict, deque
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        # Build adjacency
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        parent = [-1]*n
        order = []             # postorder stack
        stack = [0]
        parent[0] = -2         # mark root visited

        # Build parent and visitation order (preorder), then we'll process in reverse for postorder
        while stack:
            u = stack.pop()
            order.append(u)
            for v in g[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)

        # process nodes in reverse (children before parent)
        subsum_mod = [0]*n
        cuts = 0
        for u in reversed(order):
            # accumulate child's mod sums into u
            total_mod = values[u] % k
            for v in g[u]:
                if parent[v] == u:        # v is child of u
                    total_mod = (total_mod + subsum_mod[v]) % k
            subsum_mod[u] = total_mod

            # if this node's subtree mod is 0 and it's not the root, we can cut the edge to parent
            if u != 0 and subsum_mod[u] == 0:
                cuts += 1

        # Number of components = cuts + 1
        return cuts + 1
