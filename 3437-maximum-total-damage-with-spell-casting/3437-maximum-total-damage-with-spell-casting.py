from collections import Counter
from bisect import bisect_right
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        # Aggregate total damage for each unique power value
        cnt = Counter(power)
        damage_sum = {v: v * freq for v, freq in cnt.items()}

        # Sorted unique values
        vals = sorted(damage_sum.keys())
        m = len(vals)
        dp = [0] * m

        # Base case
        dp[0] = damage_sum[vals[0]]

        for i in range(1, m):
            v = vals[i]
            # find largest index j < i with vals[j] < v - 2
            # bisect_right returns first index > (v-3), so subtract 1 for j
            j = bisect_right(vals, v - 3) - 1

            take = damage_sum[v] + (dp[j] if j >= 0 else 0)
            dp[i] = max(dp[i-1], take)

        return dp[-1]
