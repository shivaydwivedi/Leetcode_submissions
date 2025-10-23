class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Keep running until only 2 digits remain
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                new_digit = (int(s[i]) + int(s[i + 1])) % 10
                new_s.append(str(new_digit))
            s = ''.join(new_s)
        
        # Check if the two remaining digits are equal
        return s[0] == s[1]
