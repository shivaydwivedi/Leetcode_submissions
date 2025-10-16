from typing import List
from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter()
        for num in nums:
            r = ((num % value) + value) % value  # handle negatives safely
            cnt[r] += 1

        mex = 0
        while True:
            r = mex % value
            if cnt[r] > 0:
                cnt[r] -= 1
                mex += 1
            else:
                break
        return mex
