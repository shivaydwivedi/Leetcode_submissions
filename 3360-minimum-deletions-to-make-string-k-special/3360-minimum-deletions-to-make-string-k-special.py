class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter
        
        freq = list(Counter(word).values())
        maxf = max(freq)
        
        ans = float('inf')
        
        # Try all possible minimum frequency x
        for x in range(maxf + 1):
            deletions = 0
            
            for f in freq:
                if f < x:
                    # delete whole frequency
                    deletions += f
                elif f > x + k:
                    # trim excessive frequency
                    deletions += f - (x + k)
                # else: f is in [x, x+k] → OK
            
            ans = min(ans, deletions)
        
        return ans