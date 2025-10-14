class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # dimensions of matrix 
        m = len(matrix) # no. of rows
        n = len(matrix[0]) # no. of columns
        # initialize boundaries
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        # store the result 
        res = []

        # condition for maintaining integrity of boudary
        while left <= right and top <= bottom:
            # traversing top row
            for i in range(left, right+1):
                res.append(matrix[top][i])
            # increment the top
            top += 1
            # traversing the right column
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            # decrement the right 
            right -= 1
            # trversing the bottom row
            if top <= bottom: # conditon to check if the boundary is updated
                for i in range(right , left-1, -1):
                    res.append(matrix[bottom][i])
                # decrement the bottom
                bottom -= 1
            # traversiing the left column
            if left <= right:  # conditon to check if the boundary is updated
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                # increment the left
                left +=1
        return res            