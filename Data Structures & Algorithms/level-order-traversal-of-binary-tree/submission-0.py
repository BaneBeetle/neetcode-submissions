# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ret = []
        if not root:
            return []
        queue = deque([root])

        while queue:
            lst = []
            for n in queue:
                lst.append(n.val)
            ret.append(lst)

            level_length = len(queue) # How many nodes are on that level

            for node in range(level_length):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        return ret


