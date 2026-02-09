# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #if empty tree
        if root is None:
            return False

        # if its a leaf node 
        if root.left is None and root.right is None:
            return targetSum == root.val
        # caculate remainign sum
        remainingsum = targetSum - root.val
        return (
            self.hasPathSum(root.left, remainingsum) or 
            self.hasPathSum(root.right, remainingsum)
        )
