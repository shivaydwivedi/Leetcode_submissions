class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # sum of n natural numbers
        nat_sum = (n*(n+1))//2
        # actual sum of numbers
        act_sum = sum(nums)
        return nat_sum - act_sum

       