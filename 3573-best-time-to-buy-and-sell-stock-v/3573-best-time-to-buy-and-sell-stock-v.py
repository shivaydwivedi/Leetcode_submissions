class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        NEG = -10**18

        # dp[t][0]=flat, dp[t][1]=long, dp[t][2]=short
        dp = [[NEG, NEG, NEG] for _ in range(k + 1)]
        dp[0][0] = 0

        for p in prices:
            for t in range(k, -1, -1):
                # open positions
                dp[t][1] = max(dp[t][1], dp[t][0] - p)  # buy
                dp[t][2] = max(dp[t][2], dp[t][0] + p)  # short sell

                # close positions
                if t + 1 <= k:
                    dp[t + 1][0] = max(
                        dp[t + 1][0],
                        dp[t][1] + p,  # sell long
                        dp[t][2] - p   # buy back short
                    )

        return max(dp[t][0] for t in range(k + 1))
