# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.all_values = []

        def dfs(current):
            
            if current is None:
                return


            left = dfs(current.left)
            self.all_values.append(current.val)
            right = dfs(current.right)

            return
        
        dfs(root)
        print(self.all_values)
        return self.all_values[k - 1]