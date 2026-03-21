class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1

        while l < r:
            # skip non-alpha num char on left 
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # compare (case insensitive)
            if s[l].lower() != s[r].lower():
                return False # mismatch
            l += 1
            r -= 1

        return True # all matched 