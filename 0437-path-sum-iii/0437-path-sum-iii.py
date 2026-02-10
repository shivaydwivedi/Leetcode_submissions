# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def countpathfrom(self,node, target):
        if node is None:
            return 0

        count = 0
        if node.val == target:
            count = 1

        count += self.countpathfrom(node.left, target-node.val)
        count += self.countpathfrom(node.right, target-node.val)

        return count


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        return (
            self.countpathfrom(root, targetSum)+
            self.pathSum(root.left, targetSum)+
            self.pathSum(root.right, targetSum)
        )