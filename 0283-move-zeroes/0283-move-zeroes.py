class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # length of the array
        n = len(nums)
        # slow pointer
        slow = 0
        # scan the array with fast
        for fast in range(0,n):
            # if a non-zero number
            if nums[fast] != 0:
                # swap it with nums[slow]
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # increment the slow pointer
                slow += 1
        # return the output
        return nums