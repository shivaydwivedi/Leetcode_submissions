class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        from collections import defaultdict
        mod = 10**9 + 7
        n = len(nums)

        left = defaultdict(int)
        right = defaultdict(int)

        # fill right count
        for x in nums:
            right[x] += 1
        
        ans = 0

        for j in range(n):
            mid = nums[j]
            right[mid] -= 1   # j cannot be used on right

            target = mid * 2

            if target in left and target in right:
                ans = (ans + left[target] * right[target]) % mod
            
            left[mid] += 1    # j now moves to left
        
        return ans % mod
