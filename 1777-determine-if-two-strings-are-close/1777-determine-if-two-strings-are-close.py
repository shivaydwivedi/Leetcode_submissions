class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # length check
        if len(word1) != len(word2):
            return False
        
        # Count frequencies
        from collections import Counter
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # compare unique character sets
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # compare sorted frequencies distribution
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True

