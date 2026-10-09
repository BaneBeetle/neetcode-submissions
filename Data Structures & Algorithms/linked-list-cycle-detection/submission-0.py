# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        current = head

        while current:
            if current not in visited:
                visited.append(current)
            else:
                print("Wait.. we have seen this node before")
                return True
            current = current.next
        
        return False