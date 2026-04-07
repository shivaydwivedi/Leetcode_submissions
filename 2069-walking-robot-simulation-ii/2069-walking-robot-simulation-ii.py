     
class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.moved = False
        # Total positions on the perimeter
        self.limit = 2 * (width + height - 2)

    def step(self, num: int) -> None:
        self.moved = True
        # Modulo allows us to skip unnecessary full laps
        self.pos = (self.pos + num) % self.limit

    def getPos(self) -> List[int]:
        p = self.pos
        # Bottom edge (Eastbound)
        if 0 <= p < self.w:
            return [p, 0]
        # Right edge (Northbound)
        elif p < self.w + self.h - 1:
            return [self.w - 1, p - (self.w - 1)]
        # Top edge (Westbound)
        elif p < 2 * self.w + self.h - 2:
            return [self.w - 1 - (p - (self.w + self.h - 2)), self.h - 1]
        # Left edge (Southbound)
        else:
            return [0, self.h - 1 - (p - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        # Special case: If the robot moves a full lap and lands on (0,0),
        # its direction is "South" because it arrived from the West.
        if self.pos == 0 and self.moved:
            return "South"
        
        p = self.pos
        if 1 <= p < self.w:
            return "East"
        elif self.w <= p < self.w + self.h - 1:
            return "North"
        elif self.w + self.h - 1 <= p < 2 * self.w + self.h - 2:
            return "West"
        else:
            # "South" if we are on the left edge, 
            # or "East" if we are at (0,0) but haven't moved yet.
            return "South" if self.moved else "East"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()