class Solution:
    def removeStars(self, s: str) -> str:
        # empty stack
        stack = []
        # traverse the string
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        final = ''.join(stack)
        return final
