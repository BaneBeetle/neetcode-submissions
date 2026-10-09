# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode], low, high) -> bool:
            
            if not node:
                return True
            elif node.val <= low or node.val >= high:
                return False
            else:
                return dfs(node.right, node.val, high) and dfs(node.left, low, node.val)
        

        return dfs(root, float('-inf'), float('inf'))