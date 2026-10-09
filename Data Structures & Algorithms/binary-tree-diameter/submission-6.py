# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.most = 0
        self.dfs(root)
        return self.most
    
    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.most = max(self.most, (left + right))

        return 1 + max(left, right)