class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # keep the count of time
        total_time = 0
        # iterate over the list
        for i in range(1,len(points)):
            # define pairs
            x1,y1 = points[i-1]
            x2,y2 = points[i]
            # distance of each dimension
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            # Max dist determines the time
            total_time += max(dx,dy)
        # return the total time
        return total_time
