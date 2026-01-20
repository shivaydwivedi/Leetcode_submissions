class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        ans = []
        for p in nums:
            if p % 2 == 0:
                ans.append(-1)
                continue

            # count trailing 1s
            k = 0
            t = p
            while t & 1:
                k += 1
                t >>= 1

            # minimal x
            x = p - (1 << (k - 1))
            ans.append(x)

        return ans
