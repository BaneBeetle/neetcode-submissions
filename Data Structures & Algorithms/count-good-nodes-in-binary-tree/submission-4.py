# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, -float("inf"))

        return self.count
    
    def dfs(self, node: TreeNode, current_max=-float("inf")):
        if node is None:
            return

        if node.val >= current_max:
            self.count += 1
        
        current_max = max(current_max, node.val)

        left = self.dfs(node.left, current_max)
        right = self.dfs(node.right, current_max)
