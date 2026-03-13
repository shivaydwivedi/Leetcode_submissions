import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def can(T):
            removed = 0
            
            for t in workerTimes:
                k = int((math.sqrt(1 + 8*T/t) - 1) // 2)
                removed += k
                if removed >= mountainHeight:
                    return True
            
            return False
        
        lo = 0
        hi = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        ans = hi
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if can(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans