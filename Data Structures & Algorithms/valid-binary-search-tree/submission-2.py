# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(current, current_min, current_max):

            if current is None:
                return True

            if not (current_min < current.val < current_max):
                print(current_min)
                print(current.val)
                print(current_max)
                return False
            
            if current.val < current_max:
                left = dfs(current.left, current_min, current.val)
            else:
                left = dfs(current.left, current_min, current_max)
            
            if current.val > current_min:
                right = dfs(current.right, current.val, current_max)
            else:
                right = dfs(current.right, current_min, current_max)
            
            return left and right
        
        return dfs(root, -9999, 9999)

