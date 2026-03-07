class Solution:
    def minFlips(self, s: str) -> int:
 
        n = len(s)
        s2 = s + s
        
        alt1 = alt2 = 0
        res = float('inf')
        
        for i in range(len(s2)):
            if s2[i] != str(i % 2):
                alt1 += 1
            if s2[i] != str((i + 1) % 2):
                alt2 += 1
            
            if i >= n:
                if s2[i - n] != str((i - n) % 2):
                    alt1 -= 1
                if s2[i - n] != str((i - n + 1) % 2):
                    alt2 -= 1
            
            if i >= n - 1:
                res = min(res, alt1, alt2)
        
        return res