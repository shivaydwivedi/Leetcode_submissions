class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0)+1

        for key in freq:
            if freq[key] == 1:
                return key
            

