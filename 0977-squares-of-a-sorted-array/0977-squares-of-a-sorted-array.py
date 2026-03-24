class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # init pointers
        l = 0
        r = n-1

        # result array 
        res = [0]*n
        # building result from left to right 
        pos = n-1
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l]**2
                l += 1
            else:
                res[pos] = nums[r]**2
                r -= 1
            pos -= 1

        return res



