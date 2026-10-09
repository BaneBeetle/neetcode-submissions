# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(current, highest):
            if current is None:
                return 0
            if highest <= current.val:
                highest = current.val
                return 1 + dfs(current.left, highest) + dfs(current.right, highest)
            else:
                return dfs(current.left, highest) + dfs(current.right, highest)
        
        return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
