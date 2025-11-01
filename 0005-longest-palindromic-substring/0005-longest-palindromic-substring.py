class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        end = 0

        # Helper function to expand around a given center
        def expandFromCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd-length palindrome (center at s[i])
            len1 = expandFromCenter(i, i)
            # Case 2: Even-length palindrome (center between s[i] and s[i+1])
            len2 = expandFromCenter(i, i + 1)

            # Take the longer palindrome length
            max_len = max(len1, len2)

            # If we found a longer palindrome, update start and end
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # Return the longest palindromic substring
        return s[start:end + 1]
