class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        n = len(strs)
        m = len(strs[0])

        # sorted[i] means strs[i] <= strs[i+1] is already confirmed
        sorted_pairs = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            delete = False

            # Check if this column breaks lexicographic order
            for i in range(n - 1):
                if not sorted_pairs[i]:
                    if strs[i][col] > strs[i + 1][col]:
                        delete = True
                        break

            if delete:
                deletions += 1
                continue

            # Update sorted pairs
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

        return deletions
