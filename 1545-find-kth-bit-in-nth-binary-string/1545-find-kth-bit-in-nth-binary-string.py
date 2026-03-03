class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        invert = 0
        
        while n > 1:
            mid = 1 << (n - 1)
            
            if k == mid:
                return str(1 ^ invert)
            
            if k > mid:
                k = (1 << n) - k
                invert ^= 1
            
            n -= 1
        
        return str(0 ^ invert)