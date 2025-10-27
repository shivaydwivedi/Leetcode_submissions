class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0      # Number of devices in the previous non-empty row
        result = 0    # Total beams count
        
        for row in bank:
            count = row.count('1')  # Count devices in current row
            if count > 0:
                result += prev * count
                prev = count        # Update previous device count
        
        return result
