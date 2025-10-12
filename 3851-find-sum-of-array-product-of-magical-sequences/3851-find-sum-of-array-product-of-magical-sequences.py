from functools import lru_cache
from math import comb
MOD = 10**9 + 7
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)

        # Precompute factorials and inverse factorials up to m for nCr (mod MOD)
        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact = [1] * (m + 1)
        invfact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def nCr_mod(nv, rv):
            if rv < 0 or rv > nv:
                return 0
            return fact[nv] * invfact[rv] % MOD * invfact[nv - rv] % MOD

        # power[i][x] = nums[i]^x % MOD for x = 0..m
        power = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for x in range(1, m + 1):
                power[i][x] = power[i][x - 1] * (nums[i] % MOD) % MOD

        # DFS over indices (pos), carry, used_bits, remaining picks
        @lru_cache(None)
        def dfs(pos, carry, used_bits, remaining):
            # If we've assigned all picks
            if remaining == 0:
                # Remaining carry may create higher set bits; count them
                # popcount of carry (carry might be > 0)
                pop = carry.bit_count()
                return 1 if (used_bits + pop) == k else 0

            # If we've exhausted indices but still have picks to allocate -> impossible
            if pos == n:
                return 0

            res = 0
            # choose x copies of index 'pos' (0..remaining)
            # multiply: power[pos][x] * C(remaining, x) * dfs(next)
            for x in range(remaining + 1):
                total = carry + x
                bit = total & 1            # lower bit contributes to used_bits
                new_carry = total >> 1     # carry to next bit (higher index)
                ways = nCr_mod(remaining, x)
                contrib = power[pos][x] * ways % MOD
                res += contrib * dfs(pos + 1, new_carry, used_bits + bit, remaining - x)
                if res >= MOD: res -= MOD

            return res % MOD

        return dfs(0, 0, 0, m) % MOD