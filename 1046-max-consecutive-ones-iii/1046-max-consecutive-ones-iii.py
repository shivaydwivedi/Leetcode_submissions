class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zero_count = 0
        max_len = 0

        for r in range(0,len(nums)):
            if nums[r] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            current_window_len = r - l + 1
            max_len = max(max_len, current_window_len)
        return max_len