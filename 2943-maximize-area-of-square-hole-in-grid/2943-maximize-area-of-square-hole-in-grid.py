class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def longest_consecutive(arr):
            if not arr:
                return 0
            arr.sort()
            best = cur = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            return best

        maxH = longest_consecutive(hBars)
        maxV = longest_consecutive(vBars)

        side = min(maxH, maxV) + 1
        return side * side
