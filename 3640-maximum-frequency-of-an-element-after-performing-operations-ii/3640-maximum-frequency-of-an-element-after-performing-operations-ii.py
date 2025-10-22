from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Count frequency of each number in the original array
        frequency_count = defaultdict(int)
      
        # Difference array to track range contributions
        # For each number x, we can change it to any value in [x-k, x+k]
        difference_array = defaultdict(int)
      
        for num in nums:
            # Count original frequency
            frequency_count[num] += 1
          
            # Initialize difference array entry for this number
            difference_array[num] += 0
          
            # Mark the range [num - k, num + k] where this number can contribute
            # +1 at the start of the range
            difference_array[num - k] += 1
            # -1 after the end of the range
            difference_array[num + k + 1] -= 1
      
        max_frequency = 0
        cumulative_sum = 0
      
        # Process points in sorted order to calculate maximum possible frequency
        for value, delta in sorted(difference_array.items()):
            # Update cumulative sum (number of elements that can be changed to current value)
            cumulative_sum += delta
          
            # Maximum frequency at this value is:
            # - Original count plus operations (limited by numOperations)
            # - Cannot exceed total available elements that can reach this value
            max_frequency = max(
                max_frequency, 
                min(cumulative_sum, frequency_count[value] + numOperations)
            )
      
        return max_frequency
