class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # initialize 
        first = float('inf')
        second = float('inf')
        # iterate through the array
        for num in nums:
            # if found new smaller
            if num <= first:
                first = num
            # if found num> second
            elif num <= second:
                second = num
            else:
                # found num > second > first
                return True
        # if no triplet found
        return False
