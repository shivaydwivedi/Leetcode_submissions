class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # length of array
        n = len(nums)
        # sort the array
        nums.sort()
        # create tre result array
        res = []
        # iterate over the array
        for i in range(n):
            # remove duplicates of i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left pointer
            l = i+1
            # right pointer
            r = n-1
            while l < r:
                # calculate the total
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else :
                    # add the triplet to the result array 
                    res.append([nums[i] , nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    # remove duplicates of l
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # remove duplicates of r
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res
