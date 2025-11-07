class Solution:
    def reverseWords(self, s: str) -> str:
        # Trim the outer spaces
        s.strip()
        # split the words
        words = s.split()
        # reverse the words
        reversed_words = words[::-1] # words.reverse()
        return ' '.join(reversed_words) # ' '.join(words)