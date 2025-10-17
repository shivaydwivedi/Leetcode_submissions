from collections import defaultdict

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        # dp0 -> no change used yet
        # dp1 -> one change already used
        dp0 = {0: 1}
        dp1 = {}

        for i in range(n):
            new0 = defaultdict(int)
            new1 = defaultdict(int)
            bit = ord(s[i]) - ord('a')

            # Case 1: No change used yet
            for mask, val in dp0.items():
                newMask = mask | (1 << bit)
                # If within k distinct chars
                if bin(newMask).count('1') <= k:
                    new0[newMask] = max(new0[newMask], val)
                else:
                    new0[1 << bit] = max(new0[1 << bit], val + 1)

                # Try changing s[i] (use our one allowed change)
                for c in range(26):
                    nmask = mask | (1 << c)
                    if bin(nmask).count('1') <= k:
                        new1[nmask] = max(new1[nmask], val)
                    else:
                        new1[1 << c] = max(new1[1 << c], val + 1)

            # Case 2: Change already used
            for mask, val in dp1.items():
                newMask = mask | (1 << bit)
                if bin(newMask).count('1') <= k:
                    new1[newMask] = max(new1[newMask], val)
                else:
                    new1[1 << bit] = max(new1[1 << bit], val + 1)

            dp0, dp1 = new0, new1  # roll states

        ans = 0
        for v in dp0.values():
            ans = max(ans, v)
        for v in dp1.values():
            ans = max(ans, v)
        return ans
