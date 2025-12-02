class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        
        MOD = 10**9 + 7
        ymap = defaultdict(int)
        
        # Count points at each y-level
        for x, y in points:
            ymap[y] += 1
        
        S = 0   # total horizontal segments
        Q = 0   # sum of squares of segments
        
        for cnt in ymap.values():
            if cnt >= 2:
                seg = cnt * (cnt - 1) // 2
                S = (S + seg) % MOD
                Q = (Q + seg * seg) % MOD
        
        # number of ways to pick 2 different horizontal segments
        ans = (S * S - Q) % MOD
        ans = ans * pow(2, MOD-2, MOD) % MOD  # divide by 2 using mod inverse
        
        return ans
