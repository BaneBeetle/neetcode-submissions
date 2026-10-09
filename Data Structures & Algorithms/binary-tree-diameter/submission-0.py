# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.highest = 0

        def dfs(current):
            if not current:
                return 0
            left = dfs(current.left)
            right = dfs(current.right)

            self.highest = max(self.highest, left)
            self.highest = max(self.highest, right)
            self.highest = max(self.highest, right + left)
            return 1 + max(left, right)
        
        dfs(root)

        return self.highest

        
