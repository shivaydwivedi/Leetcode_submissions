class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Optimised solution
        # initialize two pointers
        left = 0 # start
        right = len(height) - 1 # end
        max_area = 0 

        # start calculating with pointers
        while left < right :
            # clac widht
            width = right - left
            curr_height = min(height[right], height[left])
            area = (width)*(curr_height)
            # update the max area
            max_area = max(area, max_area)


            # move the smaller height inwards
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        
