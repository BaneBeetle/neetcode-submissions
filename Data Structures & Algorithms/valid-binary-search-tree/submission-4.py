# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        self.dfs(root, -float("inf"), float("inf"))
        return self.valid
    
    def dfs(self, node: Optional[TreeNode], current_min, current_max):
        if node is None:
            return
        
        if not (current_min < node.val < current_max):
            self.valid = False

        left = self.dfs(node.left, current_min, node.val)
        right = self.dfs(node.right, node.val, current_max)
