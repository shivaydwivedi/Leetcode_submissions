class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        MOD = 10**9 + 7

        # Include boundaries
        h = [1] + sorted(hFences) + [m]
        v = [1] + sorted(vFences) + [n]

        # Compute all possible gaps
        H = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                H.add(h[j] - h[i])

        ans = -1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in H:
                    ans = max(ans, d)

        return -1 if ans == -1 else (ans * ans) % MOD
