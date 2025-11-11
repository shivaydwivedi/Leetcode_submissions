class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # length of string
        n = len(s)
        # vowels
        vowels = { 'a', 'e', 'i', 'o', 'u'}
        # count of vowels
        count = 0
        # maximum count
        max_count = 0
        # counting vowels in first window
        for i in range(0,k):
            if s[i] in vowels:
                count += 1
            max_count = count
        # slide the window
        for i in range(k,n):
           # character leaving the window
            if s[i-k] in vowels:   
                count -= 1
            # character entering the window
            if s[i] in vowels:
                count += 1
            max_count = max(max_count, count)
        return max_count

