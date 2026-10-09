"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Post Order = left right root
        ret = []

        # This time, children is a list of nodes

        def dfs(node: 'Node'):
            if not node:
                return

            for child in node.children:
                dfs(child)
            ret.append(node.val)

        

        dfs(root)
        return ret
