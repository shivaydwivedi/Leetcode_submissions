class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # 1) strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        p = i

        # 2) strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == p or i == n - 1:
            return False
        q = i

        # 3) strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
