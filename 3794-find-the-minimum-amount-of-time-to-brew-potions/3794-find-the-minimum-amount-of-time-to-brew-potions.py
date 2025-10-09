from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        
        # Compute prefix for first potion
        prev_prefix = [0] * n
        total = 0
        for i in range(n):
            total += skill[i] * mana[0]
            prev_prefix[i] = total
        
        start = 0
        
        # Process each next potion one by one
        for j in range(1, m):
            curr_prefix = [0] * n
            total = 0
            for i in range(n):
                total += skill[i] * mana[j]
                curr_prefix[i] = total
            
            # Compute gap between potion j-1 and potion j
            gap = 0
            for i in range(n):
                left = prev_prefix[i]
                right = curr_prefix[i - 1] if i > 0 else 0
                gap = max(gap, left - right)
            
            start += gap
            prev_prefix = curr_prefix  # reuse memory reference
        
        return start + prev_prefix[-1]
