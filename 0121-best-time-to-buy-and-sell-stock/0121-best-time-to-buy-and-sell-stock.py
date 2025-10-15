class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # buy pointer
        right = 1 # sell pointer
        max_profit = 0 # max profit 

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right]- prices[left]
                max_profit = max(profit, max_profit)
            else: 
                # if found a new lower price than current one 
                # update the but pointer
                left = right
            # move the right pointer
            right +=1
        return max_profit