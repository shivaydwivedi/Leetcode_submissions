class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        parent = list(range(row * col + 2))
        TOP = row * col
        BOTTOM = row * col + 1

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        grid = [[0] * col for _ in range(row)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Process in reverse
        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            grid[r][c] = 1
            idx = r * col + c

            # Union with neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    union(idx, nr * col + nc)

            # Union with virtual nodes
            if r == 0:
                union(idx, TOP)
            if r == row - 1:
                union(idx, BOTTOM)

            if find(TOP) == find(BOTTOM):
                return day
