class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # guard condition
        if len(s2) < len(s1):
            return False

        # track frequencies of both the strings
        from collections import defaultdict

        count1 = defaultdict(int)
        count2 = defaultdict(int)

        # frequncies of s1
        for c in s1:
            count1[c] += 1

        # left boundary of window
        left = 0

        # right boundary of window
        for right in range(len(s2)):
            # frequencies of s2
            count2[s2[right]] += 1

            # winodw validity condition 
            if right - left + 1 > len(s1):
                count2[s2[left]] -= 1
                # remove 0 comparisonm condition 
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1
            # comparison

            if count2 == count1:
                return True 

        return False