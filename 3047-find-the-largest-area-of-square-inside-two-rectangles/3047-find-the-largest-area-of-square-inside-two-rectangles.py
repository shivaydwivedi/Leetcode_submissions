class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:

        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                ix1 = max(x1, x3)
                iy1 = max(y1, y3)
                ix2 = min(x2, x4)
                iy2 = min(y2, y4)

                if ix2 > ix1 and iy2 > iy1:
                    side = min(ix2 - ix1, iy2 - iy1)
                    ans = max(ans, side * side)

        return ans
