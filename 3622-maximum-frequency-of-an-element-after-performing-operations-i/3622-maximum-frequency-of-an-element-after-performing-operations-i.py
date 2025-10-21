from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0

        mini = min(nums)
        maxi = max(nums)
        result = 0

        # Frequency prefix sum array
        freq = [0] * (maxi + 2)  # +2 to safely handle freq[curr - 1]

        for i in nums:
            freq[i] += 1

        # Build prefix sum
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        for curr in range(mini, maxi + 1):
            l = max(mini, curr - k)
            r = min(maxi, curr + k)
            f = freq[curr] - freq[curr - 1]  # freq of curr
            extra = min(numOperations, freq[r] - freq[l - 1] - f)
            result = max(result, f + extra)

        return result
