class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
 
        m, n = len(grid), len(grid[0])
        
        bal = [[0]*n for _ in range(m)]
        cntX = [[0]*n for _ in range(m)]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                bal[i][j] = val
                cntX[i][j] = 1 if grid[i][j] == 'X' else 0
                
                if i > 0:
                    bal[i][j] += bal[i-1][j]
                    cntX[i][j] += cntX[i-1][j]
                if j > 0:
                    bal[i][j] += bal[i][j-1]
                    cntX[i][j] += cntX[i][j-1]
                if i > 0 and j > 0:
                    bal[i][j] -= bal[i-1][j-1]
                    cntX[i][j] -= cntX[i-1][j-1]
                
                if bal[i][j] == 0 and cntX[i][j] > 0:
                    ans += 1
        
        return ans