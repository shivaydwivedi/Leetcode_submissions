class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: remove leading and trailing spaces
        s = s.strip()
        
        # Step 2: split by whitespace (handles multiple spaces)
        words = s.split()
        
        # Step 3: reverse the list of words
        words.reverse()
        
        # Step 4: join them back with single space
        return ' '.join(words)