class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        m, n = len(mat), len(mat[0])

        # Build prefix sum
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i+1][j+1] = (
                    ps[i][j+1] + ps[i+1][j] - ps[i][j] + mat[i][j]
                )

        def exists(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    s = ps[i+k][j+k] - ps[i][j+k] - ps[i+k][j] + ps[i][j]
                    if s <= threshold:
                        return True
            return False

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if exists(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
