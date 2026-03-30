class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array 
        nums.sort()
        # result array 
        res = []
        
        # set one number and prevent duplicates
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
        # define pointers
            l , r = i+1, len(nums)-1  
        # iterate over the array 
            while l < r:
                total = nums[i] + nums[l] + nums[r]

            # total = 0 condition
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l > r and nums[r] == nums[r-1]:
                        r += 1
                
                    l += 1
                    r -= 1
            
            # total < 0 
                elif total < 0:
                    l += 1
            # total > 0
                else: 
                    r -= 1

        return res


