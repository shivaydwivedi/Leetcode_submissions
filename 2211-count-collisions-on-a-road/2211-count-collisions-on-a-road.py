class Solution:
    def countCollisions(self, directions: str) -> int:
        s = directions
        
        # Remove L's from the left (they escape and never collide)
        i = 0
        while i < len(s) and s[i] == 'L':
            i += 1
        
        # Remove R's from the right (they escape and never collide)
        j = len(s) - 1
        while j >= 0 and s[j] == 'R':
            j -= 1
        
        # Now every remaining L or R must collide exactly once
        collisions = 0
        for k in range(i, j + 1):
            if s[k] != 'S':
                collisions += 1
        
        return collisions