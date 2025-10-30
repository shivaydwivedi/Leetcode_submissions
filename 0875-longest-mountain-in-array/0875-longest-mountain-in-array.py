class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        n = len(arr)
        if n < 3:
            return 0
        
        max_length = 0
        i = 1  # Start at index 1 (can't be peak at 0)
        
        while i < n - 1:  # Can't be peak at last index
            # Check if current position is a peak
            is_peak = arr[i-1] < arr[i] > arr[i+1]
            
            if is_peak:
                # Expand left boundary
                left = i
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                
                # Expand right boundary
                right = i
                while right < n - 1 and arr[right] > arr[right+1]:
                    right += 1
                
                # Calculate mountain length
                current_length = right - left + 1
                max_length = max(max_length, current_length)
                
                # Jump to end of mountain (optimization)
                i = right
            else:
                i += 1
        
        return max_length
