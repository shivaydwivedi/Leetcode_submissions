class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Two pinbters approach

        n = len(s)

        # left booundary
        left = 0

        # track character in current window
        char_set = set()
        # max length
        max_len = 0


        # move the right poiter
        for right in range(n): 
            # if the new character is already in the set(means duplicate)
            while s[right] in char_set:
                # remove the leftmost character 
                char_set.remove(s[left])
                # move the window one step from left 
                left += 1
            # if no duplicate add the new element
            char_set.add(s[right]) 

            # update the maximum length 
            # current window size right-left+1

            max_len = max(max_len, right - left + 1)
        return max_len