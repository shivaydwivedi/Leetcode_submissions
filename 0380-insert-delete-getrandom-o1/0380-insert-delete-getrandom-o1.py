
import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}   # val -> index in arr

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        idx = self.pos[val]
        last_val = self.arr[-1]

        # Move last element to idx
        self.arr[idx] = last_val
        self.pos[last_val] = idx

        # Remove last element
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()