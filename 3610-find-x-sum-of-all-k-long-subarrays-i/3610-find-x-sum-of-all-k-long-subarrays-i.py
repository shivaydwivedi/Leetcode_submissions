from collections import Counter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        res = []

        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)
            
            # Sort by (-frequency, -value)
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            
            # Take top x
            top_x = sorted_items[:x]
            
            # Sum all occurrences of these top x numbers
            total = sum(num * count for num, count in freq.items() if num in [t[0] for t in top_x])
            
            res.append(total)
        
        return res
