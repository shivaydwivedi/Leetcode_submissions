class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = energy[:]  # copy initial values

        # Process from right to left
        for i in range(n - 1 - k, -1, -1):
            dp[i] += dp[i + k]

        return max(dp)
