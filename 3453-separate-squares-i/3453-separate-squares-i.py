class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        total_area = 0.0
        low = float('inf')
        high = float('-inf')

        for _, y, l in squares:
            total_area += l * l
            low = min(low, y)
            high = max(high, y + l)

        target = total_area / 2.0

        def area_below(Y):
            s = 0.0
            for _, y, l in squares:
                if Y <= y:
                    continue
                elif Y >= y + l:
                    s += l * l
                else:
                    s += (Y - y) * l
            return s

        # Binary search for Y
        for _ in range(60):  # enough for 1e-6 precision
            mid = (low + high) / 2
            if area_below(mid) < target:
                low = mid
            else:
                high = mid

        return low
