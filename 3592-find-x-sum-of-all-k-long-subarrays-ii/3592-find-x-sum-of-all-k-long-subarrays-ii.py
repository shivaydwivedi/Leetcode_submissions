from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        freq = defaultdict(int)
        top = SortedList()   # stores (-freq, -val)
        rest = SortedList()
        sum_top = 0
        res = []

        def add_element(val):
            nonlocal sum_top
            old_freq = freq[val]
            new_freq = old_freq + 1
            freq[val] = new_freq

            if old_freq > 0:
                entry = (-old_freq, -val)
                if entry in top:
                    top.remove(entry)
                    sum_top -= old_freq * val
                else:
                    rest.remove(entry)
            
            new_entry = (-new_freq, -val)
            rest.add(new_entry)
            rebalance()

        def remove_element(val):
            nonlocal sum_top
            old_freq = freq[val]
            new_freq = old_freq - 1

            entry = (-old_freq, -val)
            if entry in top:
                top.remove(entry)
                sum_top -= old_freq * val
            else:
                rest.remove(entry)

            if new_freq > 0:
                freq[val] = new_freq
                rest.add((-new_freq, -val))
            else:
                del freq[val]

            rebalance()

        def rebalance():
            nonlocal sum_top
            # Move from rest to top
            while len(top) < x and rest:
                f, v = rest.pop(0)
                top.add((f, v))
                sum_top += (-f) * (-v)
            
            # Ensure top has only x highest
            while len(top) > x:
                f, v = top.pop(-1)
                rest.add((f, v))
                sum_top -= (-f) * (-v)
            
            # Fix order if needed
            while rest and top and rest[0] < top[-1]:
                f1, v1 = rest.pop(0)
                f2, v2 = top.pop(-1)
                sum_top -= (-f2) * (-v2)
                sum_top += (-f1) * (-v1)
                rest.add((f2, v2))
                top.add((f1, v1))

        # Initialize first window
        for i in range(k):
            add_element(nums[i])
        res.append(sum_top)

        # Slide window
        for i in range(k, len(nums)):
            add_element(nums[i])
            remove_element(nums[i - k])
            res.append(sum_top)

        return res
