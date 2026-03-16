class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()

        for i in range(m):
            for j in range(n):
                res.add(grid[i][j])
                k = 1
                
                while True:
                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break
                    
                    s = 0
                    
                    x, y = i-k, j
                    for d in range(k):
                        s += grid[x+d][y+d]
                    
                    x, y = i, j+k
                    for d in range(k):
                        s += grid[x+d][y-d]
                    
                    x, y = i+k, j
                    for d in range(k):
                        s += grid[x-d][y-d]
                    
                    x, y = i, j-k
                    for d in range(k):
                        s += grid[x-d][y+d]
                    
                    res.add(s)
                    k += 1

        return sorted(res, reverse=True)[:3]