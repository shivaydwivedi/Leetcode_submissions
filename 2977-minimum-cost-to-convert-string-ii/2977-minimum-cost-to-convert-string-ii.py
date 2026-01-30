import heapq
from collections import defaultdict

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int]
    ) -> int:

        n = len(source)
        INF = 10**18

        # 1) Build string graph
        graph = defaultdict(list)
        strings = set(original) | set(changed)

        for o, c, w in zip(original, changed, cost):
            if len(o) == len(c):
                graph[o].append((c, w))

        # 2) Dijkstra from each original string
        min_cost = defaultdict(dict)

        for s in strings:
            pq = [(0, s)]
            dist = {s: 0}

            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist.get(v, INF):
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))

            min_cost[s] = dist

        # 3) DP over source
        dp = [INF] * (n + 1)
        dp[n] = 0

        # Pre-group originals by length
        by_len = defaultdict(list)
        for o in original:
            by_len[len(o)].append(o)

        for i in range(n - 1, -1, -1):
            # Skip if characters already match
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            for L, words in by_len.items():
                if i + L > n:
                    continue

                src_sub = source[i:i + L]
                tgt_sub = target[i:i + L]

                if src_sub in min_cost and tgt_sub in min_cost[src_sub]:
                    dp[i] = min(dp[i],
                                min_cost[src_sub][tgt_sub] + dp[i + L])

        return -1 if dp[0] == INF else dp[0]
