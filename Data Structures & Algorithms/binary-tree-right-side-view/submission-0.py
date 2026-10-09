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
        
        queue = deque([root])

        while queue:
            ret.append(queue[-1].val) # hopefully this is an integer? grab the last element from the queue

            level_length = len(queue) # how many node currently at the level

            for i in range(level_length): # auto stop wheneever we visited all nodes from the level
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ret
        