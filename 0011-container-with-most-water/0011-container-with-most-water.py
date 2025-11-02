class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Optimised solution
        n = len(height)
        l = 0 # left pointer
        r = n-1 # right pointer
        max_area = 0 # maximum area
        while l < r:
            # calculate area between lines
            width = r - l # width
            height_limit = min(height[l], height[r]) # height
            area = height_limit * width
            # update max_area if needed
            max_area = max(area, max_area)
            # move the shorter heighted pointer
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area