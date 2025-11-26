class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[j][r] for current row
        dp = [ [0]*k for _ in range(n) ]

        # Initialize row 0 (only moves from left)
        first_mod = grid[0][0] % k
        dp[0][first_mod] = 1
        for j in range(1, n):
            val_mod = grid[0][j] % k
            for r in range(k):
                if dp[j-1][r]:
                    dp[j][ (r + val_mod) % k ] = (dp[j][ (r + val_mod) % k ] + dp[j-1][r]) % MOD

        # Process remaining rows
        for i in range(1, m):
            new_dp = [ [0]*k for _ in range(n) ]

            # column 0: only from top (dp[0])
            val_mod = grid[i][0] % k
            for r in range(k):
                if dp[0][r]:
                    new_dp[0][ (r + val_mod) % k ] = (new_dp[0][ (r + val_mod) % k ] + dp[0][r]) % MOD

            # other columns: from top (dp[j]) and left (new_dp[j-1])
            for j in range(1, n):
                val_mod = grid[i][j] % k

                # from top
                for r in range(k):
                    if dp[j][r]:
                        new_dp[j][ (r + val_mod) % k ] = (new_dp[j][ (r + val_mod) % k ] + dp[j][r]) % MOD

                # from left (new_dp[j-1])
                for r in range(k):
                    if new_dp[j-1][r]:
                        new_dp[j][ (r + val_mod) % k ] = (new_dp[j][ (r + val_mod) % k ] + new_dp[j-1][r]) % MOD

            dp = new_dp

        return dp[n-1][0] % MOD