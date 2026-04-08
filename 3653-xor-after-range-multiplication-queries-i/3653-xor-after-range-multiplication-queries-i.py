class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Process each query sequentially
        for l, r, k, v in queries:
            # We start at l and increment by k as long as we don't exceed r
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
        
        # Calculate the bitwise XOR sum of the final array
        xor_sum = 0
        for x in nums:
            xor_sum ^= x
            
        return xor_sum