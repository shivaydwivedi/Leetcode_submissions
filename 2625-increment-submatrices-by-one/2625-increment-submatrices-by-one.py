class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Apply 2D difference increments
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Build prefix sums row-wise
        for r in range(n):
            for c in range(n):
                diff[r][c] += diff[r][c - 1] if c > 0 else 0

        # Build prefix sums column-wise
        for c in range(n):
            for r in range(n):
                diff[r][c] += diff[r - 1][c] if r > 0 else 0

        # Extract final n x n matrix
        mat = [[diff[r][c] for c in range(n)] for r in range(n)]
        return mat
