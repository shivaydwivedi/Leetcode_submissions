class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # feasibilty function
        def feasible(cap):
            days_needed=1
            load = 0
            for w in weights:
                if load+ w > cap:
                    days_needed +=1
                    load = 0
                load += w
            return days_needed <= days
        # Binary search oundaries
        # initialize low and high
        lo = max(weights)
        hi = sum(weights)
        # find capacity
        
        while lo<hi:
            mid = (lo+hi)//2
            # check if capacity works [cap = mid]
            if feasible(mid):
                hi = mid
            else:
                lo = mid+1
            # minimum weight ship could transport
        return lo