# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.all_values = [] # iterate thru the entire tree post-order put them here
        # see if its not sorted or its sorted

        def dfs(current):
            if current is None:
                return
            
            left = dfs(current.left)
            self.all_values.append(current.val)
            right = dfs(current.right)

            return
        
        dfs(root)
        copy = sorted(self.all_values)
        print(copy)
        print(self.all_values)
        return (copy == self.all_values) and (len(set(copy)) == len(self.all_values))
