class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        import bisect

        # Sort by end time
        events.sort(key=lambda x: x[1])

        n = len(events)
        ends = [events[i][1] for i in range(n)]

        # Prefix max of values
        max_value = [0] * n
        max_value[0] = events[0][2]

        for i in range(1, n):
            max_value[i] = max(max_value[i - 1], events[i][2])

        ans = 0

        for i in range(n):
            start, end, val = events[i]

            # Best single event
            ans = max(ans, val)

            # Find last event that ends before start
            idx = bisect.bisect_left(ends, start) - 1

            if idx >= 0:
                ans = max(ans, val + max_value[idx])

        return ans
