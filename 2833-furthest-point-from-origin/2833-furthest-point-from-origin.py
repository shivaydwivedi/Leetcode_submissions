class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = moves.count('L')
        r_count = moves.count('R')
        blank_count = moves.count('_')
    
    # The absolute difference between L and R plus all blanks
        return abs(l_count - r_count) + blank_count