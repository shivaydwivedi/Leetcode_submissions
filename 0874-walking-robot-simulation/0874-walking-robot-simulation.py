class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        # Directions: North, East, South, West
        # dx, dy correspond to these 4 directions
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        # Initial state
        x = y = 0
        direction = 0 # Starting North
        max_dist_sq = 0
        
        # Convert obstacles to a set of tuples for O(1) lookup
        obstacle_set = {tuple(o) for o in obstacles}
        
        for cmd in commands:
            if cmd == -1: # Turn Right
                direction = (direction + 1) % 4
            elif cmd == -2: # Turn Left
                direction = (direction + 3) % 4
            else: # Move forward 'cmd' units
                for _ in range(cmd):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    
                    if (next_x, next_y) in obstacle_set:
                        break # Stop moving in this direction
                    
                    x, y = next_x, next_y
                    # Update max distance squared at every valid step
                    max_dist_sq = max(max_dist_sq, x*x + y*y)
                    
        return max_dist_sq