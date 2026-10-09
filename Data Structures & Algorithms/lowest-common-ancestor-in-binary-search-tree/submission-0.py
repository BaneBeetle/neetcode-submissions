# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(current, p, q):
            if current is None:
                return None

            if current.val >= p.val and current.val <= q.val:
                return current
            elif current.val <= p.val and current.val >= q.val:
                return current

            return dfs(current.left, p, q) or dfs(current.right, p, q)
        
        return dfs(root, p, q)