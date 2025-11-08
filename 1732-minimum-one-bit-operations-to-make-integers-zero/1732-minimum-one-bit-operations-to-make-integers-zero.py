class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans ^= n      # Gray-code accumulation step
            n >>= 1       # Shift right for next bit group
        return ans