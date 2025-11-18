class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        
        while i < n - 1:  # stop before last bit
            if bits[i] == 1:
                i += 2     # two-bit character
            else:
                i += 1     # one-bit character

        return i == n - 1  # did we land exactly on last?