class Solution:
    def maxSumTrionic(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0

        NEG = -10**18

        inc = NEG     # valid only after an actual increase
        dec = NEG     # valid only after inc + decrease
        inc2 = NEG    # valid only after dec + increase

        ans = NEG

        for i in range(1, n):
            a, b = nums[i - 1], nums[i]

            if b > a:
                # increasing
                new_inc = max(inc + b, a + b)
                new_inc2 = dec + b if dec != NEG else NEG

                inc = new_inc
                inc2 = max(inc2 + b if inc2 != NEG else NEG, new_inc2)
                dec = NEG

            elif b < a:
                # decreasing
                new_dec = inc + b if inc != NEG else NEG

                dec = max(dec + b if dec != NEG else NEG, new_dec)
                inc = NEG
                inc2 = NEG

            else:
                # equal breaks strictness
                inc = dec = inc2 = NEG

            if inc2 != NEG:
                ans = max(ans, inc2)

        return ans if ans != NEG else 0
