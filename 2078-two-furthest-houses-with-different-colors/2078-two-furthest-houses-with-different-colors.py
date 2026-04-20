class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        n = len(colors)
        max_dist = 0
    
    # Scan from the right to find the furthest house different from colors[0]
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
            
    # Scan from the left to find the furthest house different from colors[n-1]
        for i in range(n):
            if colors[i] != colors[n-1]:
                max_dist = max(max_dist, (n - 1) - i)
                break
            
        return max_dist