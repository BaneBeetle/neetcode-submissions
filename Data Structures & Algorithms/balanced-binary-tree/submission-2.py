# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        def dfs(current):

            if not current:
                return 0
            print("test")
            
            left = dfs(current.left)
            right = dfs(current.right)


            print("current difference", right - left)
            if abs(right - left) > 1:
                print("Hit")
                self.flag = False
                return -1

            return 1 + max(left, right)
        
        dfs(root)
        if self.flag is False:
            return False

        return True


        