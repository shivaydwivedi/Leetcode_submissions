class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # horizontal cut
        curr = 0
        for i in range(m):
            curr += sum(grid[i])
            if curr == target:
                return True
        
        # vertical cut
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
        
        curr = 0
        for j in range(n):
            curr += col_sums[j]
            if curr == target:
                return True
        
        return False