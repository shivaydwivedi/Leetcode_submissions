class Solution:
    def validPalindrome(self, s: str) -> bool:
        # function to check if palindrome or not
        def is_pal(l,r):
            # iterate over the whole string
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True 

        n = len(s)
        # init pointer 
        l = 0
        r = n-1


        while l < r:
            # if you find a mismatch 
            if s[l] != s[r]:
                # skip right element or left element 
                # until it turns into a palindrome
                return is_pal(l+1,r) or is_pal(l, r-1)
            l += 1
            r -= 1
        return True



 

