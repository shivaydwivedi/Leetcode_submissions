import bisect

class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new = [left, right]
        i = bisect.bisect_left(self.intervals, new)

        if i > 0 and self.intervals[i-1][1] >= left:
            i -= 1

        while i < len(self.intervals) and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            self.intervals.pop(i)

        self.intervals.insert(i, [left, right])

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.intervals, [left, float('inf')]) - 1
        if i >= 0 and self.intervals[i][0] <= left and self.intervals[i][1] >= right:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.intervals, [left, right])

        if i > 0:
            i -= 1

        while i < len(self.intervals):
            start, end = self.intervals[i]

            if start >= right:
                break

            if end <= left:
                i += 1
                continue

            self.intervals.pop(i)

            if start < left:
                self.intervals.insert(i, [start, left])
                i += 1

            if end > right:
                self.intervals.insert(i, [right, end])
                break

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)