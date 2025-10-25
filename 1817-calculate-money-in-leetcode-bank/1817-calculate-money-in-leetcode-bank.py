class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        
        # total from complete weeks
        total = 28 * weeks + 7 * (weeks * (weeks - 1)) // 2
        
        # remaining days of the partial week
        start = weeks + 1
        for i in range(days):
            total += start + i
        
        return total
