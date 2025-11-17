class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1   # store previous index where 1 appeared
        
        for i, x in enumerate(nums):
            if x == 1:
                if prev != -1 and (i - prev - 1) < k:
                    return False
                prev = i
        
        return True