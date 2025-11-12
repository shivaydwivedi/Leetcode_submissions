class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # unique elements in both array
        set1 = set(nums1)
        set2 = set(nums2)
        # Set difference
        diff1 = set1 - set2 # element only in nums1
        diff2 = set2 - set1 # element only in nums2
        return [list(diff1), list(diff2)]