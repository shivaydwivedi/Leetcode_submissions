class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        ans = []

        for p in nums:
            # Even numbers cannot be formed
            if p % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s
            k = 0
            t = p
            while t & 1:
                k += 1
                t >>= 1

            # Remove the highest trailing 1
            x = p - (1 << (k - 1))
            ans.append(x)

        return ans
