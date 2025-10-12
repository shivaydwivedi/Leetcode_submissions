class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sort the array
        nums_sorted = sorted(nums)
        # map 
        index_map = {}
        # iterate over the array 
        for i , num in enumerate(nums_sorted):
            # take each number
            if num not in index_map:
                # map its index to its value
                index_map[num] = i
        # reorder the map to original orientation
        return [index_map[num] for num in nums]
