class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        
        def simulate(start, direction):
            arr = nums[:]  # copy array
            curr = start
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += direction
                else:
                    arr[curr] -= 1
                    direction *= -1
                    curr += direction
            return all(x == 0 for x in arr)
        
        result = 0
        for i, val in enumerate(nums):
            if val == 0:
                if simulate(i, 1):   # try right
                    result += 1
                if simulate(i, -1):  # try left
                    result += 1
        return result
