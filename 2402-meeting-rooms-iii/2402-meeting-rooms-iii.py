class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        import heapq

        # Sort meetings by original start time
        meetings.sort()

        # Min-heap of available rooms
        available = list(range(n))
        heapq.heapify(available)

        # Min-heap of busy rooms: (end_time, room)
        busy = []

        # Count meetings per room
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free rooms that have finished before current meeting starts
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Assign immediately
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Delay meeting
                end_time, room = heapq.heappop(busy)
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        # Return room with max meetings (tie → smallest index)
        return count.index(max(count))
