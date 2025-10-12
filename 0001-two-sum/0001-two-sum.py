class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # define an empty dictionary(or hashmap)
        mp = {}
        # iterate through the array with index 
        for i, n in enumerate(nums):
          #  define complement
            complement = target - n 
            # if the (target-n) is present in the dictionary
            if complement in mp:
                # return the index of complement and the compatible partner
                return mp[complement], i  
            # Else the add the number with index to the dictionary
            mp[n] = i