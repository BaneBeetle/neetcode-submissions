# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        queue = deque([root])
        ret = []

        while queue:
            level_size = len(queue)

            for _ in range(len(queue)): # one lvl at a time
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
                    if _ == level_size  - 1:
                        ret.append(node.val)

        
        return ret