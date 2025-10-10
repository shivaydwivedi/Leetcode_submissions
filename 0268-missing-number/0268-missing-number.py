class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nat_sum = (n*(n+1))//2
        act_sum = sum(nums)
        return nat_sum - act_sum

       