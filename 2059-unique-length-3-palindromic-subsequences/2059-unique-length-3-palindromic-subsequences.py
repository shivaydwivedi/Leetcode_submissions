class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        
        # Find first and last occurrence of each char
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        
        result = 0
        
        # For each character as outer palindrome char
        for c in range(26):
            if first[c] != -1 and last[c] != -1 and first[c] < last[c]:
                L = first[c]
                R = last[c]
                
                # Count distinct middle characters
                mids = set(s[L+1:R])
                result += len(mids)
        
        return result
