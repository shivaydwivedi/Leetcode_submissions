class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        r1 = x
        r2 = x + k - 1
        c1 = y
        c2 = y + k - 1
        
        for i in range(k // 2):
            for j in range(c1, c2 + 1):
                grid[r1 + i][j], grid[r2 - i][j] = grid[r2 - i][j], grid[r1 + i][j]
        
        return grid