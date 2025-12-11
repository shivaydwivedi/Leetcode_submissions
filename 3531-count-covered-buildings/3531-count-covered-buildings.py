class Solution:
    def countCoveredBuildings(self, n, buildings):
        from collections import defaultdict
        
        rows = defaultdict(list)
        cols = defaultdict(list)

        # Group by rows and columns
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        # Precompute min/max for each row and column
        row_min = {}
        row_max = {}
        col_min = {}
        col_max = {}

        for r, ys in rows.items():
            row_min[r] = min(ys)
            row_max[r] = max(ys)

        for c, xs in cols.items():
            col_min[c] = min(xs)
            col_max[c] = max(xs)

        # Count covered buildings
        ans = 0
        for x, y in buildings:
            if row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]:
                ans += 1

        return ans
