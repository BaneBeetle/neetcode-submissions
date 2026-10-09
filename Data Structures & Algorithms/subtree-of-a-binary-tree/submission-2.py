# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, tree, subtree):
        if not tree and not subtree:
            return True
        if (tree and subtree) and (tree.val == subtree.val):
            # check the left side
            return self.sameTree(tree.left, subtree.left) and self.sameTree(tree.right, subtree.right)
        
        return False
        
        

            
