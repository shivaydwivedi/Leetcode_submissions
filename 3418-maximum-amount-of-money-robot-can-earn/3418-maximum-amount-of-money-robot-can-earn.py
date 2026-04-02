class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = max coins at (i,j) with k neutralizations used
        dp = [[[-10**18]*3 for _ in range(n)] for _ in range(m)]
        
        # start cell
        val = coins[0][0]
        dp[0][0][0] = val
        if val < 0:
            dp[0][0][1] = 0  # neutralize
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == -10**18:
                        continue
                    
                    for di, dj in [(1,0),(0,1)]:
                        ni, nj = i+di, j+dj
                        if ni >= m or nj >= n:
                            continue
                        
                        val = coins[ni][nj]
                        
                        # Case 1: don't neutralize
                        dp[ni][nj][k] = max(
                            dp[ni][nj][k],
                            dp[i][j][k] + val
                        )
                        
                        # Case 2: neutralize
                        if val < 0 and k < 2:
                            dp[ni][nj][k+1] = max(
                                dp[ni][nj][k+1],
                                dp[i][j][k]
                            )
        
        return max(dp[m-1][n-1])