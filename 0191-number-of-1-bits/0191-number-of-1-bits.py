class Solution:
    def hammingWeight(self, n: int) -> int:
        str = bin(n)

        counter = str.count('1')

        return counter
