class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        import heapq
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # dist[i][j][t] = min cost to reach (i,j) using t teleports
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        # Collect and sort cells by value
        cells = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort()

        # For each teleport layer, track which cells are already activated
        activated = [0] * (k + 1)

        pq = [(0, 0, 0, 0)]  # cost, i, j, teleports_used

        while pq:
            cost, i, j, t = heapq.heappop(pq)
            if cost > dist[i][j][t]:
                continue

            # Normal moves
            for ni, nj in ((i+1, j), (i, j+1)):
                if ni < m and nj < n:
                    new_cost = cost + grid[ni][nj]
                    if new_cost < dist[ni][nj][t]:
                        dist[ni][nj][t] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj, t))

            # Teleport moves
            if t < k:
                ptr = activated[t]
                while ptr < len(cells) and cells[ptr][0] <= grid[i][j]:
                    _, x, y = cells[ptr]
                    if dist[x][y][t+1] > cost:
                        dist[x][y][t+1] = cost
                        heapq.heappush(pq, (cost, x, y, t+1))
                    ptr += 1
                activated[t] = ptr

        return min(dist[m-1][n-1])
