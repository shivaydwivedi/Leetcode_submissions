class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_increasing(sub):
            # check if the given subarray is strictly increasing
            for i in range(1, len(sub)):
                if sub[i] <= sub[i - 1]:
                    return False
            return True
        
        n = len(nums)
        
        # iterate through all valid starting indices
        for i in range(n - 2 * k + 1):
            if is_increasing(nums[i:i + k]) and is_increasing(nums[i + k:i + 2 * k]):
                return True
        
        return False
