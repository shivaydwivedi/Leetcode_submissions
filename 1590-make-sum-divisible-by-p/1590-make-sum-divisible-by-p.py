class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0

        mp = {0: -1}  # remainder → index
        pref = 0
        ans = float('inf')

        for i, x in enumerate(nums):
            pref = (pref + x) % p
            target = (pref - need) % p

            if target in mp:
                ans = min(ans, i - mp[target])

            mp[pref] = i

        return ans if ans < len(nums) else -1