class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Hashmap Approach
        #seen = {}
        #for num in nums:
           # if num in seen :
         #       return True 
         #   seen[num] = True
        #return False
        # Set Approach
        return len(nums) != len(set(nums))
