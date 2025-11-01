class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a set to track unique 
        seen = set()
        # left pointer 
        left = 0 
        # maximum length 
        max_len = 0
        # length of string
        n = len(s)
        # iterate through the string
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left +1)
        return max_len