
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        max_points = 0

        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1
            xi, yi = points[i]

            for j in range(i + 1, n):
                xj, yj = points[j]

                if xi == xj and yi == yj:
                    duplicates += 1
                else:
                    dx = xj - xi
                    dy = yj - yi

                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    # Normalize sign
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    elif dx == 0:
                        dy = 1   # vertical line
                    elif dy == 0:
                        dx = 1   # horizontal line

                    slopes[(dy, dx)] += 1

            local_max = 0
            for count in slopes.values():
                local_max = max(local_max, count)

            max_points = max(max_points, local_max + duplicates)

        return max_points
