class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        
        needed = 1 << k
        seen = set()
        mask = 0
        all_bits = (1 << k) - 1
        
        for i in range(n):
            mask = ((mask << 1) & all_bits) | (s[i] == '1')
            
            if i >= k - 1:
                seen.add(mask)
                if len(seen) == needed:
                    return True
        
        return False