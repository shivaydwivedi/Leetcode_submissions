class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        count = 0

        # Helper to check if a 3x3 grid is magic
        def is_magic(r, c):
            # Center must be 5
            if grid[r + 1][c + 1] != 5:
                return False

            seen = set()
            for i in range(3):
                for j in range(3):
                    val = grid[r + i][c + j]
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)

            # Check rows and columns
            for i in range(3):
                if sum(grid[r + i][c:c + 3]) != 15:
                    return False
                if sum(grid[r + k][c + i] for k in range(3)) != 15:
                    return False

            # Check diagonals
            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15:
                return False
            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15:
                return False

            return True

        # Scan all possible 3x3 subgrids
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1

        return count
