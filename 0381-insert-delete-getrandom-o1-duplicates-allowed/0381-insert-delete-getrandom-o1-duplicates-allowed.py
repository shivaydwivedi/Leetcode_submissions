
import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.pos = defaultdict(set)  # val -> set of indices

    def insert(self, val: int) -> bool:
        self.arr.append(val)
        self.pos[val].add(len(self.arr) - 1)
        return len(self.pos[val]) == 1  # True if first occurrence

    def remove(self, val: int) -> bool:
        if not self.pos[val]:
            return False
        
        # Get one index of val
        remove_idx = self.pos[val].pop()
        last_val = self.arr[-1]

        # Move last element to remove_idx
        self.arr[remove_idx] = last_val
        self.pos[last_val].add(remove_idx)
        self.pos[last_val].discard(len(self.arr) - 1)

        # Remove last element
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()