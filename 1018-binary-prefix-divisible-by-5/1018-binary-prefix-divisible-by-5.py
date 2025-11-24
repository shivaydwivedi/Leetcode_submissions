class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        curr = 0
        
        for b in nums:
            curr = (curr * 2 + b) % 5
            result.append(curr == 0)
        
        return result