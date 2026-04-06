class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return []

        from collections import defaultdict

        count_s = defaultdict(int)
        count_p = defaultdict(int)

        for c in p:
            count_p[c] += 1
        left = 0
        for right in range(len(s)):
            count_s[s[right]] += 1

            if right - left + 1 > len(p):
                count_s[s[left]] -= 1
                if count_s[s[left]] == 0:
                    del count_s[s[left]] 
                left += 1
            if count_p == count_s:
                res.append(left)
        return res