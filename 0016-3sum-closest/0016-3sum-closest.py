class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort the array 
        nums.sort()
        # store closest
        closest = float('inf')

        # fix one element
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1

            # iterate
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                # compare the target to closest
                if abs(target - total) < abs(target-closest):
                    closest = total

                # pointer moveement
                if total < target :
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        return closest
