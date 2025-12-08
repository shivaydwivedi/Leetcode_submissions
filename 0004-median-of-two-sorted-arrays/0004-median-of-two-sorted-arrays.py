from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        total = n + m

        
        half = (total + 1) // 2

        left, right = 0, n

        while left <= right:
            i = (left + right) // 2     # number taken from nums1 (cut in nums1)
            j = half - i                # number taken from nums2 (cut in nums2)

            # Boundaries around the cuts. Use -inf/+inf for out-of-range.
            left1  = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i]   if i < n else float('inf')

            left2  = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j]   if j < m else float('inf')

            # If this partition is correct (all left <= all right)
            if left1 <= right2 and left2 <= right1:
                # If total is odd => median is the largest on the left side
                if total % 2 == 1:
                    return float(max(left1, left2))

                # If total is even => median is average of two middle values
                return (max(left1, left2) + min(right1, right2)) / 2.0

            # If left1 is too big, move cut in nums1 left
            elif left1 > right2:
                right = i - 1

            # else left1 is too small, move cut right
            else:
                left = i + 1

        return 0
