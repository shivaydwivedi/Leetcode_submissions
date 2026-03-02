class Solution:
    def minPartitions(self, n: str) -> int:

        max_digit = 0
        for ch in n:
            max_digit = max(max_digit, ord(ch) - 48)
        return max_digit