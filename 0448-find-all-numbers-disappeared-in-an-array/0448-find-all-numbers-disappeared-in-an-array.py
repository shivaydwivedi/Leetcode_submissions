class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # length of array 
        n = len(nums)
        # make set of the given array
        nums_set = set(nums)
        # make a missing list
        missing = []
        # iterate through the array
        for i in range(1,n+1):
            # if number is in set 
            if i not in nums_set:
                # add it to the missing list
                missing.append(i)
            # return missing list
        return missing
        
        