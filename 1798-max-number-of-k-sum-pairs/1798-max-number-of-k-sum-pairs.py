
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sort the array 
        nums.sort()
        # initialize our pointers
        l = 0
        r = len(nums)-1
        pairs = 0
        # cALCULATE The sum 
        while l < r:
            sum = nums[l] + nums[r]
            # sum < k
            if sum < k:
                l += 1
            # sum > k
            elif sum > k:
                r -= 1
            # sum == k
            else:
                pairs += 1
                l += 1
                r -= 1
        return pairs