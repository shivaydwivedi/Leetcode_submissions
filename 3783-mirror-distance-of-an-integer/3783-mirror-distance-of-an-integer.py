class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        rev = 0
        
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        
        return abs(original - rev)
