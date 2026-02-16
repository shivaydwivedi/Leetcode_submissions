
import bisect

class SummaryRanges:

    def __init__(self):
        self.intervals = []  # list of [start, end]

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        new_interval = [value, value]

        i = bisect.bisect_left(intervals, new_interval)

        # Merge with left interval if needed
        if i > 0 and intervals[i - 1][1] + 1 >= value:
            i -= 1

        while i < len(intervals) and intervals[i][0] - 1 <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            intervals.pop(i)

        intervals.insert(i, new_interval)

    def getIntervals(self):
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()