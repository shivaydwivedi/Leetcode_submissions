class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # total sum
        total_sum = sum(nums)
        left_sum = 0
        for i in range(0, len(nums)):
            if (2*(left_sum)) + nums[i] == total_sum:
                # pivot found
                return i
            left_sum += nums[i]
        # no pivot found
        return -1