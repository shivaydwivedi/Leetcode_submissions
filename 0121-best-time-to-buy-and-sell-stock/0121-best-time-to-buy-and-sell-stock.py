class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')  # Cheapest price seen so far
        max_profit = 0            # Best profit so far
    
        for price in prices:
            # Update minimum price (a.k.a.best day to buy)
            if price < min_price:
                min_price = price
            
            # Calculate profit if we sell today
            profit = price - min_price
            
            # Update max profit
            if profit > max_profit:
                max_profit = profit
        
        return max_profit