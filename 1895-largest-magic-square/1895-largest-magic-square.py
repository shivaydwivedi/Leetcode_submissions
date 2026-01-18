class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        # Prefix sums
        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*n for _ in range(m+1)]
        diag1 = [[0]*(n+1) for _ in range(m+1)]
        diag2 = [[0]*(n+2) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]
                diag1[i+1][j+1] = diag1[i][j] + grid[i][j]
                diag2[i+1][j] = diag2[i][j+1] + grid[i][j]

        max_k = min(m, n)

        for k in range(max_k, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row[i][j+k] - row[i][j]

                    # Check rows
                    ok = True
                    for r in range(i, i+k):
                        if row[r][j+k] - row[r][j] != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    # Check columns
                    for c in range(j, j+k):
                        if col[i+k][c] - col[i][c] != target:
                            ok = False
                            break
                    if not ok:
                        continue

                    # Check diagonals
                    if diag1[i+k][j+k] - diag1[i][j] != target:
                        continue
                    if diag2[i+k][j] - diag2[i][j+k] != target:
                        continue

                    return k

        return 1
