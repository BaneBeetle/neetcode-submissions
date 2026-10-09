# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, current):

            if not node:
                return False
    
            current += node.val

            if not node.left and not node.right:
                return current == targetSum
            else:
                return dfs(node.left, current) or dfs(node.right, current)



        return dfs(root, 0)
        
