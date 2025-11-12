from math import gcd

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Check overall gcd
        overall_gcd = nums[0]
        for num in nums[1:]:
            overall_gcd = gcd(overall_gcd, num)
        if overall_gcd != 1:
            return -1

        # Step 2: If 1 already exists
        if 1 in nums:
            return n - nums.count(1)

        # Step 3: Find shortest subarray with gcd == 1
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break  # no need to extend further
        return (min_len - 1) + (n - 1)
