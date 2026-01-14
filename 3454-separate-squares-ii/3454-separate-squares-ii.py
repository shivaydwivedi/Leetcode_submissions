class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()

        # Active x-intervals
        active = []
        prev_y = events[0][0]
        total_area = 0

        def union_x(intervals):
            if not intervals:
                return 0
            intervals.sort()
            res = 0
            cur_l, cur_r = intervals[0]
            for l, r in intervals[1:]:
                if l > cur_r:
                    res += cur_r - cur_l
                    cur_l, cur_r = l, r
                else:
                    cur_r = max(cur_r, r)
            return res + (cur_r - cur_l)

        # First pass: compute total union area
        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                total_area += dy * union_x(active)
            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))
            prev_y = y

        target = total_area / 2

        # Second pass: find y where area reaches target
        active.clear()
        prev_y = events[0][0]
        curr_area = 0

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            if dy > 0:
                width = union_x(active)
                if width > 0:
                    next_area = curr_area + dy * width
                    if next_area >= target:
                        return prev_y + (target - curr_area) / width
                    curr_area = next_area
            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))
            prev_y = y

        return prev_y