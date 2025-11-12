class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # current altitude
        curr = 0
        # maximum altitude
        max_alt = 0
        # go through the array
        for g in gain:
            curr = curr + g
            max_alt = max(max_alt, curr)
        return max_alt
      
      