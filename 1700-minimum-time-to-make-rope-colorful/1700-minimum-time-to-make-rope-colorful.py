class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        prev_time = neededTime[0]  # time of last kept balloon
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # Remove the smaller one
                total_time += min(prev_time, neededTime[i])
                # Keep the larger one for next comparison
                prev_time = max(prev_time, neededTime[i])
            else:
                prev_time = neededTime[i]
        
        return total_time
