class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialization 
        count = {} # to keep count of each character 
        left = 0# start of the window
        max_freq = 0 # maximum freq of the elements
        max_len = 0 # answer

        # Expanding the window -> by moving right 
        for right in range(len(s)):
            # adding the new new character to the window
            count[s[right]] = count.get(s[right],0)+1
            # updateing the frequency
            max_freq = max(max_freq, count[s[right]])
            # checking the validity
            wind_size = right - left + 1
            # invalid condition
            if wind_size - max_freq > k:
                # shrink the window 
                count[s[left]] - = 1
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len


