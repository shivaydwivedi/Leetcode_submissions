class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ans = 0
        n = len(s)

        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:  # ch == '0'
                # if this zero is the end of a zero-block (next char is '1' or it's the last char)
                if i + 1 == n or s[i + 1] == '1':
                    ans += ones
        return ans