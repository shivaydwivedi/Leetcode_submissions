class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        n = len(nums)

        # slow pointer
        s = 0

        # move through the array
        for f in range(0,n):
            if nums[f] != 0:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1
        return nums
