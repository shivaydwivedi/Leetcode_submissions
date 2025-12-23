# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## recurisve helper function
        def height(node):
            ## if current node is None
            if not node:
                return 0
            
            # calculating height of left subtree
            left = height(node.left)
            # if left tree i already unbalanced
            if left == -1:
                
                return -1
            
            # calculate height of right subtree
            right = height(node.right)
            # if right is already unbalanced
            if right == -1:
                return -1
            
            # if difference in left and right subtree is greater than 1
            if abs(left - right) > 1:
                return -1
            
            # balcned return height 
            # Height = (current node) + MAX dist(left or right)
            return 1 + max(left, right)
        
        return height(root) != -1