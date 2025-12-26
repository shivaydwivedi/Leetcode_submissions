class Solution:
    def bestClosingTime(self, customers: str) -> int:

        # Initial penalty: shop closed all day
        penalty = customers.count('Y')

        min_penalty = penalty
        best_hour = 0

        # Try closing at hour j = 1 to n
        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1   # no longer closed-with-customers
            else:  # c == 'N'
                penalty += 1   # now open-with-no-customers

            # Check if this is a better (or earlier) closing time
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1

        return best_hour
