class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total = sum(batteries)

        # Binary search T (maximum running time)
        left, right = 0, total // n

        while left < right:
            mid = (left + right + 1) // 2  # try larger T
            need = mid * n

            # total usable power capped at mid
            have = 0
            for b in batteries:
                if b >= mid:
                    have += mid
                else:
                    have += b

            if have >= need:
                left = mid  # feasible
            else:
                right = mid - 1

        return left
