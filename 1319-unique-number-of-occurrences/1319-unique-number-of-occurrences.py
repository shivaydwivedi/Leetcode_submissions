from collections import Counter
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # count frequency of each element
        count = Counter(arr)
        # check uniqueness
        return len(count.values()) == len(set(count.values()))