class Solution:
    def minOperations(self, s: str) -> int:
        mismatch0 = 0
        mismatch1 = 0
        
        for i, c in enumerate(s):
            expected0 = str(i % 2)
            expected1 = str(1 - (i % 2))
            
            if c != expected0:
                mismatch0 += 1
            if c != expected1:
                mismatch1 += 1
        
        return min(mismatch0, mismatch1)