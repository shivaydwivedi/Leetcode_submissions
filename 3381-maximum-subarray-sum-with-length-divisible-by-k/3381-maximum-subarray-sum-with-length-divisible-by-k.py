class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix = 0
        # best minimum prefix for each remainder class
        best = [10**30] * k  
        best[0] = 0  # prefix sum before starting
        
        ans = -10**30
        
        for i, x in enumerate(nums, start=1):
            prefix += x
            r = i % k

            # try using best prefix with same remainder
            ans = max(ans, prefix - best[r])

            # update the best minimum prefix for this remainder
            best[r] = min(best[r], prefix)

        return ans
