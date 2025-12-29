class Solution:
    def pyramidTransition(self, bottom: str, allowed):
        from collections import defaultdict

        # Build transition map
        trans = defaultdict(list)
        for pat in allowed:
            trans[(pat[0], pat[1])].append(pat[2])

        memo = {}

        def dfs(row):
            # If reduced to one block, pyramid is complete
            if len(row) == 1:
                return True

            if row in memo:
                return memo[row]

            # Generate all possible next rows
            def backtrack(i, next_row):
                if i == len(row) - 1:
                    return dfs(next_row)

                pair = (row[i], row[i + 1])
                if pair not in trans:
                    return False

                for ch in trans[pair]:
                    if backtrack(i + 1, next_row + ch):
                        return True

                return False

            memo[row] = backtrack(0, "")
            return memo[row]

        return dfs(bottom)
