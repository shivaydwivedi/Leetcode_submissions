class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for x in nums:
            if x % 3 != 0:
                ops += 1
        return ops