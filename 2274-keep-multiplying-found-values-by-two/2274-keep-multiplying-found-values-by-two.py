class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)  # O(n)

        while original in s:
            original *= 2

        return original