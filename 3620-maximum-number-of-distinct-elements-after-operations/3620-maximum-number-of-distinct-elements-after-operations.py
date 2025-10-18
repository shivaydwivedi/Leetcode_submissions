class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        current = -10**18  # very small starting value

        for x in nums:
            start = x - k
            end = x + k

            # Move current pointer if it's behind the start
            if current < start:
                current = start

            # If we can assign a value <= end, do it
            if current <= end:
                count += 1
                current += 1  # next distinct number must be larger

        return count
