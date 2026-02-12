

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            freq = [0] * 26
            distinct = 0
            
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                
                # check balanced
                counts = [f for f in freq if f > 0]
                if len(set(counts)) == 1:
                    ans = max(ans, j - i + 1)
        
        return ans