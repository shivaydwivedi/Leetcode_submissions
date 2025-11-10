class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # initialize both pointers
        i = 0
        j = 0
        # check through the array
        while i < len(s) and j < len(t):
            # if character in both string matches
            if s[i] == t[j]:
                # increment i pointer
                i += 1
            # if they don't match 
            # increment j pointer
            j += 1
        # if i reaches the lenght of s string
        if i == len(s):
            return True
        else:
            return False