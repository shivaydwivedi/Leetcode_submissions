class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)

        # compute prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stations[i]

        # initial power for each city with range r
        power = [0] * n
        for i in range(n):
            L = max(0, i - r)
            R = min(n - 1, i + r)
            power[i] = pref[R + 1] - pref[L]

        # feasibility check: can we make every city have at least 'target' power with <= k added stations?
        def can(target: int) -> bool:
            add_diff = [0] * (n + 1)  # difference array for added-power ranges
            curAdded = 0
            used = 0

            for i in range(n):
                curAdded += add_diff[i]             # accumulate current additions
                cur = power[i] + curAdded
                if cur < target:
                    need = target - cur
                    used += need
                    if used > k:
                        return False
                    # place the need stations at pos = min(i + r, n-1)
                    pos = min(i + r, n - 1)
                    L = max(0, pos - r)
                    R = min(n - 1, pos + r)
                    add_diff[L] += need
                    add_diff[R + 1] -= need
                    # Since L <= i (pos <= i + r => pos - r <= i), the current city is immediately affected
                    curAdded += need
            return True

        lo, hi = 0, sum(stations) + k
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
