class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def is_sorted(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

        ops = 0
        arr = nums[:]

        while not is_sorted(arr):
            min_sum = float('inf')
            idx = 0

            for i in range(len(arr) - 1):
                s = arr[i] + arr[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # merge the chosen pair
            arr[idx] = arr[idx] + arr[idx + 1]
            arr.pop(idx + 1)
            ops += 1

        return ops
