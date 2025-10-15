from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        # compute inc_len: length of strictly increasing run starting at i
        inc_len = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_len[i] = inc_len[i + 1] + 1

        # helper: check whether some k is feasible
        def can(k: int) -> bool:
            # need two adjacent blocks of length k -> i ranges 0..n-2k
            limit = n - 2 * k
            if limit < 0:
                return False
            for i in range(limit + 1):
                if inc_len[i] >= k and inc_len[i + k] >= k:
                    return True
            return False

        # binary search the maximum k in [1, n//2]
        lo, hi = 1, n // 2
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
