# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0
        stack = [(root, 0)]
        
        while stack:
            node, val = stack.pop()
            val = (val << 1) | node.val
            
            if not node.left and not node.right:
                total += val
            else:
                if node.right:
                    stack.append((node.right, val))
                if node.left:
                    stack.append((node.left, val))
        
        return total