class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # length of matrix
        m = len(matrix)
        n = len(matrix[0]) # top-right corner
        # define rows and columns
        r = 0
        c = n-1
        while r < m and c>= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                # go down
                c -= 1
            else:
                # go left
                r += 1
        return False