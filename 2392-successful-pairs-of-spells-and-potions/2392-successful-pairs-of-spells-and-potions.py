import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        m = len(potions)
        res = []
        
        for spell in spells:
            # Minimum potion strength needed
            required = (success + spell - 1) // spell  # ceiling division
            idx = bisect.bisect_left(potions, required)
            count = m - idx
            res.append(count)
            
        return res
