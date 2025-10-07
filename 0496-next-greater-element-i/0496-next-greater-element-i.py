class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Optimised approach
        # O(n+m)
        n = len(nums1)
        m = len(nums2)
        # making a map of the numbers in nums1
        nums1_indx = {num: i for i, num in enumerate(nums1)}
        # result array pre-loaded with -1
        res = [-1]*n

        # creating an empty stack
        stack = []

        # iterating over the nums2
        for i in range(m):
            cur = nums2[i]
            while stack and cur> stack[-1]:
                val = stack.pop()
                indx = nums1_indx[val]
                res[indx]= cur
            if cur in nums1_indx:
                stack.append(cur)
        return res