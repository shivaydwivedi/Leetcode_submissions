from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # empty hashmap
        counts = Counter()
        # track no. of pairs
        pairs = 0

        # iterate over the array
        for x in nums:
            # complement
            y = k-x
            if counts[y]>0:
                pairs += 1
                counts[y] -= 1
            else:
                counts[x] += 1
        return pairs
