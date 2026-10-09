"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy = Node(0)
        tail = dummy

        hash_map = {}

        # First Pass, create output w/o random and populate hash_map
        ptr = head
        while ptr:
            tail.next = Node(ptr.val, ptr.next) # ignore random
            hash_map[ptr] = tail.next
            tail = tail.next
            ptr = ptr.next

        # Second Pass, update output using filled hash_map

        ptr = head

        while ptr:
            hash_map[ptr].random = None
            if ptr.random:
                hash_map[ptr].random = hash_map[ptr.random]

            ptr = ptr.next


        return dummy.next