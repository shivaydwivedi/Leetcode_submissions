# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node,rem_sum,path,result):
            # if tree is empty
            if node is None:
                return
            # else add path
            path.append(node.val)

            # cal remaning sum
            rem_sum = rem_sum - node.val
            # if you find leaf node
            if node.left is None and node.right is None:
                # and remaining sum is zero 
                if rem_sum == 0:
                    # add the path to result list
                    result.append(path[:])

            else:
                # recursively search on left and right branches
                dfs(node.left, rem_sum, path , result)
                dfs(node.right, rem_sum, path , result)
            # remove last element from the path (backtracking)
            path.pop()


        # calls
        result = []
        path = []
        dfs(root, targetSum, path, result)
        return result
