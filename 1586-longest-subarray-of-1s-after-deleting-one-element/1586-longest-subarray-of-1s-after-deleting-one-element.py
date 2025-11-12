class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # initialize 
        l = 0
        zero_count = 0
        max_len = 0
        # start the window
        for r in range(0,len(nums)):
            if nums[r] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1 # shrink the window
            max_len = max(max_len, (r-l+1))
        return (max_len-1)
