from typing import List
import math

class Solution:
    MOD = 10**9 + 7

    def modPow(self, base, exp):
        result = 1
        base %= self.MOD
        while exp > 0:
            if exp & 1:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            exp >>= 1
        return result

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        threshold = int(math.sqrt(n))
        
        groups = [[] for _ in range(threshold)]
        
        # Process queries
        for left, right, step, value in queries:
            if step < threshold:
                groups[step].append((left, right, value))
            else:
                i = left
                while i <= right:
                    nums[i] = (nums[i] * value) % self.MOD
                    i += step
        
        # Process small step groups
        diff = [1] * (n + threshold)
        
        for step in range(1, threshold):
            if not groups[step]:
                continue
            
            # reset diff
            for i in range(len(diff)):
                diff[i] = 1
            
            # apply difference logic
            for left, right, value in groups[step]:
                diff[left] = (diff[left] * value) % self.MOD
                
                stop = left + ((right - left) // step + 1) * step
                diff[stop] = (diff[stop] * self.modPow(value, self.MOD - 2)) % self.MOD
            
            # prefix multiplication
            for i in range(step, n):
                diff[i] = (diff[i] * diff[i - step]) % self.MOD
            
            # apply to nums
            for i in range(n):
                nums[i] = (nums[i] * diff[i]) % self.MOD
        
        # final XOR
        ans = 0
        for x in nums:
            ans ^= x
        
        return ans