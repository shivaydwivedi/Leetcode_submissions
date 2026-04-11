class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter 

        need = Counter(t) # window for smaller string 
        window = {} # window for bigger string 

        have = 0 # char that match
        need_count = len(need) # required char

        # left prointer
        left = 0
        min_len = float('inf')
        res = [-1,-1]

        # expand the winbdow 
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0)+1 


            # check if requirements met
            if c in need and window[c] == need[c]:
                have += 1

            # shrink when valid 
            while have == need_count:
                # update min_len
                if (right-left+1) < min_len:
                    min_len = right-left+1
                    res = [left,right]
                # shrink window 
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        l,r = res
        return s[l:r+1] if min_len != float('inf') else ''