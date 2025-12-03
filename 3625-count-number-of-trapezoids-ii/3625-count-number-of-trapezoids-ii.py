from collections import defaultdict
from math import gcd

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(points)

        # --------------------------------------------------
        # STEP 1: Group segments by slope and *line constant*
        # slope_map[(dy,dx)][c] = list of segments (i,j)
        # --------------------------------------------------
        slope_map = defaultdict(lambda: defaultdict(list))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                # Normalize slope
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                # Compute line constant: dy*x - dx*y
                c = dy * x1 - dx * y1
                slope_map[(dy, dx)][c].append((i, j))

        # --------------------------------------------------
        # STEP 2: Count pairs of segments with same slope
        #         but *different* parallel lines
        #         (slope_pairs)
        # --------------------------------------------------
        slope_pairs = 0

        for line_dict in slope_map.values():
            seg_counts = []
            total = 0

            # count segments per-line
            for segs in line_dict.values():
                k = len(segs)
                if k >= 1:
                    total += k
                    seg_counts.append(k)

            if total < 2:
                continue

            # total segment pairs
            total_pairs = total * (total - 1) // 2

            # subtract pairs from same line
            same_line = 0
            for k in seg_counts:
                same_line += k * (k - 1) // 2

            slope_pairs = (slope_pairs + (total_pairs - same_line)) % MOD

        # --------------------------------------------------
        # STEP 3: Count parallelograms using midpoint rule
        # mid_map[(x1+x2, y1+y2)][(dy,dx)] += 1
        # --------------------------------------------------
        mid_map = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                mid = (x1 + x2, y1 + y2)

                dx = x2 - x1
                dy = y2 - y1
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                slope = (dy, dx)
                mid_map[mid][slope] += 1

        parallelograms = 0

        for slope_cnts in mid_map.values():
            t = 0
            sq = 0
            for cnt in slope_cnts.values():
                t += cnt
                sq += cnt * cnt

            parallelograms = (parallelograms + (t * t - sq) // 2) % MOD

        # final trapezoids
        return (slope_pairs - parallelograms) % MOD
