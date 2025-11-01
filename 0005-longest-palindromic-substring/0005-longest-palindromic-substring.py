class Solution:
    def longestPalindrome(self, s: str) -> str:
        # max length 
        max_len = 0
        # longest substring
        longest = " "
        n = len(s)
        # iterate through the string 
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(substring) > max_len:
                    max_len = len(substring)
                    longest = substring
        return longest
