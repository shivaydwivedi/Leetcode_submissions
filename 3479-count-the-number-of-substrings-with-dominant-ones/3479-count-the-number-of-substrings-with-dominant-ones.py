class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # prefix sum of ones
        pref1 = [0] * (n + 1)
        for i in range(n):
            pref1[i+1] = pref1[i] + (1 if s[i] == '1' else 0)

        zero_pos = [i for i,ch in enumerate(s) if ch == '0']
        zlen = len(zero_pos)

        ans = 0
        zp = 0  # pointer to first zero index >= i

        for i in range(n):
            # advance zp so zero_pos[zp] >= i (or zp == zlen)
            while zp < zlen and zero_pos[zp] < i:
                zp += 1

            # Z = 0 case: substrings starting at i with zero zeros
            next_zero_idx = zero_pos[zp] if zp < zlen else n
            # j in [i, next_zero_idx-1] have zero zeros
            ans += (next_zero_idx - i)

            # Z >= 1
            # we only need to try up to Zmax (≈200) or until zeros run out
            # but also not more than remaining zeros
            maxZ = min(200, zlen - zp)
            for Z in range(1, maxZ + 1):
                left = zero_pos[zp + Z - 1]   # earliest j having Z zeros
                # right bound is just before the (Z+1)-th zero if exists, else n-1
                if zp + Z < zlen:
                    right = zero_pos[zp + Z] - 1
                else:
                    right = n - 1

                need = Z * Z

                # ones in [i..left]
                ones_left = pref1[left + 1] - pref1[i]
                if ones_left >= need:
                    # all j in [left..right] qualify
                    ans += (right - left + 1)
                    continue

                # otherwise binary search in [left+1 .. right] to find smallest pos with ones >= need
                lo, hi = left + 1, right
                pos = -1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    ones_mid = pref1[mid + 1] - pref1[i]
                    if ones_mid >= need:
                        pos = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1

                if pos != -1:
                    ans += (right - pos + 1)
                # else none in [left..right] satisfy ones >= need, move on

        return ans