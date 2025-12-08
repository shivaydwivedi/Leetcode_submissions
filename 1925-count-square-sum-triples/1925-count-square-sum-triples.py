import math

class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n+1):
            aa = a*a
            for b in range(1, n+1):
                s = aa + b*b
                c = math.isqrt(s)
                if c*c == s and c <= n:
                    cnt += 1
        return cnt
