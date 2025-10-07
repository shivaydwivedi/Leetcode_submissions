class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        nums1_indx = {num: i for i, num in enumerate(nums1)}
        res = [-1] * n

        for i in range(m):
            if nums2[i] not in nums1_indx:
                continue
            for j in range(i + 1, m):
                if nums2[j] > nums2[i]:
                    indx = nums1_indx[nums2[i]]
                    res[indx] = nums2[j]
                    break

        return res
