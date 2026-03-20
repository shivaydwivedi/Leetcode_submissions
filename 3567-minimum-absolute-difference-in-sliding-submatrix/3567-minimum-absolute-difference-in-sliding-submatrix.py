from sortedcontainers import SortedList
from collections import Counter

class Solution:
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        res = [[0]*(n-k+1) for _ in range(m-k+1)]
        
        for i in range(m-k+1):
            freq = Counter()
            sl = SortedList()
            
            def add(x):
                if freq[x] == 0:
                    sl.add(x)
                freq[x] += 1
            
            def remove(x):
                freq[x] -= 1
                if freq[x] == 0:
                    sl.remove(x)
            
            def get_min():
                if len(sl) <= 1:
                    return 0
                ans = float('inf')
                for i in range(1, len(sl)):
                    ans = min(ans, sl[i] - sl[i-1])
                return ans
            
            # build first window
            for x in range(i, i+k):
                for y in range(k):
                    add(grid[x][y])
            
            res[i][0] = get_min()
            
            # slide right
            for j in range(1, n-k+1):
                for x in range(i, i+k):
                    remove(grid[x][j-1])
                    add(grid[x][j+k-1])
                
                res[i][j] = get_min()
        
        return res