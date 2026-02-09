# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxsofar):
            if node is None:
                return 0
            count = 0
            if node.val>= maxsofar:
                count = 1
                maxsofar = node.val

            count += dfs(node.left, maxsofar)
            count += dfs(node.right, maxsofar)

            return count
        return dfs( root, root.val)