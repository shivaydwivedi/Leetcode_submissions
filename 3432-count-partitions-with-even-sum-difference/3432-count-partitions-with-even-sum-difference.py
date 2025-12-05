class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        S = sum(nums)
        return 0 if (S & 1) else (len(nums) - 1)