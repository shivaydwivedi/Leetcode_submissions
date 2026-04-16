from typing import List
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        
        res = []
        
        for q in queries:
            arr = pos[nums[q]]
            
            if len(arr) == 1:
                res.append(-1)
                continue
            
            i = bisect_left(arr, q)
            best = float('inf')
            
            # previous neighbor
            prev_idx = arr[i-1] if i > 0 else arr[-1]
            d = abs(q - prev_idx)
            best = min(best, d, n - d)
            
            # next neighbor
            next_idx = arr[i+1] if i < len(arr)-1 else arr[0]
            d = abs(next_idx - q)
            best = min(best, d, n - d)
            
            res.append(best)
        
        return res