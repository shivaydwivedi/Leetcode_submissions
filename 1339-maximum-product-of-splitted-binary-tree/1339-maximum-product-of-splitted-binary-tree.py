# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        MOD = 10**9 + 7

        # Step 1: compute total sum
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)
        self.best = 0

        # Step 2: compute subtree sums + maximize product
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subtree = node.val + left + right
            self.best = max(self.best, subtree * (total - subtree))

            return subtree

        dfs(root)
        return self.best % MOD
