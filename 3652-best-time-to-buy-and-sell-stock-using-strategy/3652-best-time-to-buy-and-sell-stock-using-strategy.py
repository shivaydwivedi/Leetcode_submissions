class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Step 1: Base profit
        base_profit = sum(strategy[i] * prices[i] for i in range(n))

        # Step 2: Gain arrays
        gain0 = [-strategy[i] * prices[i] for i in range(n)]
        gain1 = [(1 - strategy[i]) * prices[i] for i in range(n)]

        # Step 3: Prefix sums
        pref0 = [0] * (n + 1)
        pref1 = [0] * (n + 1)

        for i in range(n):
            pref0[i + 1] = pref0[i] + gain0[i]
            pref1[i + 1] = pref1[i] + gain1[i]

        # Step 4: Sliding window
        half = k // 2
        best_gain = 0

        for start in range(n - k + 1):
            mid = start + half
            end = start + k

            gain = (pref0[mid] - pref0[start]) + (pref1[end] - pref1[mid])
            best_gain = max(best_gain, gain)

        return base_profit + best_gain
