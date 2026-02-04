# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collectleaves(node, list):
            if node is None:
                return
            if node.left == None and node.right == None:
                list.append(node.val)
                return
            collectleaves(node.left,list)
            collectleaves(node.right,list)

        leaves1 = []
        leaves2 = []

        collectleaves(root1,leaves1)
        collectleaves(root2,leaves2)

        return leaves1 == leaves2
