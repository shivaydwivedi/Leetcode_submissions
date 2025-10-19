from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_op(t: str) -> str:
            chars = list(t)
            for i in range(1, len(chars), 2):  # odd indices
                chars[i] = str((int(chars[i]) + a) % 10)
            return ''.join(chars)

        def rotate_op(t: str) -> str:
            return t[-b:] + t[:-b]

        visited = set([s])
        queue = deque([s])
        smallest = s

        while queue:
            cur = queue.popleft()
            smallest = min(smallest, cur)

            # Operation 1: add to odd indices
            added = add_op(cur)
            if added not in visited:
                visited.add(added)
                queue.append(added)

            # Operation 2: rotate right by b
            rotated = rotate_op(cur)
            if rotated not in visited:
                visited.add(rotated)
                queue.append(rotated)

        return smallest
