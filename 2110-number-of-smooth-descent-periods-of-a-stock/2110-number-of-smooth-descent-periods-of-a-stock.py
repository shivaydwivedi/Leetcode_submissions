class Solution:
    def getDescentPeriods(self, prices):
        ans = 0
        curr = 0

        for i in range(len(prices)):
            if i > 0 and prices[i - 1] - prices[i] == 1:
                curr += 1
            else:
                curr = 1
            ans += curr

        return ans
