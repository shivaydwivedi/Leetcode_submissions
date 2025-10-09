class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # must be positive, power of two, and the single bit must be in an even position
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
