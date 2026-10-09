# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ret = []

        if not root:
            return ret


        queue = deque([root]) # this is at level 1

        while queue:
            ret.append(queue[-1].val)

            level_length = len(queue) # how many nodes are in that level

            for i in range(level_length):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        
        return ret


