class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        n = len(grid)

        top = 0
        front = 0
        side = 0

        for i in range(n):
            front += max(grid[i])          # front view (rows)
            for j in range(n):
                if grid[i][j] > 0:
                    top += 1               # top view

        for j in range(n):
            side += max(grid[i][j] for i in range(n))  # side view (columns)

        return top + front + side
