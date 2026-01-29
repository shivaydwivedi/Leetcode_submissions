# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # counteer to track max depth
        max_depth = 0

        # Traverse the tree 
        def traverse(node, current_depth):
            
            nonlocal max_depth
            # check if tree is empty
            if node is None:
                return
            

            # if tree is not empty
            current_depth += 1

            # if you find leaf node
            if node.left is None and node.right is None:
                max_depth = max(max_depth, current_depth)
            
            # find depth of both sides
            traverse(node.right, current_depth)
            traverse(node.left, current_depth)
        
        
        traverse(root, 0)
        return max_depth
