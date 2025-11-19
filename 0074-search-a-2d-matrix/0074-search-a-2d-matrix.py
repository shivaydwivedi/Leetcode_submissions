class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # define rows and colums
        m = len(matrix)
        n = len(matrix[0])
        # binary search range
        l = 0
        r = (m*n)-1
        # Binary Search'
        while l <= r:
            # calc mid
            mid = (l+r)//2
            # convert 1D index -> 2D positions
            row = mid//n
            col = mid%n
            # calculate the found value
            value = matrix[row][col]
            # search for target
            if value == target:
                return True
            elif value<target:
                # check right
                l = mid+1
            else:
                # check left
                r = mid-1
        return False