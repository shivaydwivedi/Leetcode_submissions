class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: count trailing zeros for each row
        trailing = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: greedy placement
        for i in range(n):
            required = n - 1 - i
            j = i
            
            while j < n and trailing[j] < required:
                j += 1
            
            if j == n:
                return -1
            
            swaps += (j - i)
            
            # bubble row up
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                j -= 1
        
        return swaps