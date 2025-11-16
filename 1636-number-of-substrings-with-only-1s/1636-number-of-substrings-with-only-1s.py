class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        count = 0
        
        for ch in s:
            if ch == '1':
                count += 1
            else:
                ans += count * (count + 1) // 2
                count = 0
        
        # add last block if ended with '1'
        ans += count * (count + 1) // 2
        
        return ans % MOD