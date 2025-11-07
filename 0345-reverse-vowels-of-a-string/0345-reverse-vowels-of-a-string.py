class Solution:
    def reverseVowels(self, s: str) -> str:
        # make a set of vowels 
        vowels = set('aeiouAEIOU')
        # string  -> list
        s = list(s)
        # define two pointers
        left = 0
        right = len(s)-1
        while left < right:
            # set left pointer
            while left < right and s[left] not in vowels:
                left += 1
            # set right pointer
            while left < right and s[right] not in vowels:
                right -= 1
            # swap left and right vowel
            s[left] , s[right] = s[right] , s[left]
            #move left and right pointer inwards
            left += 1
            right -= 1
        # return the string 
        return "".join(s)