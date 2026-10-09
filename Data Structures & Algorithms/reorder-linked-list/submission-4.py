# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find the midpoint
        dummy = ListNode()
        tail = dummy

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Seperate the list, reverse the second half

        half = slow.next
        slow.next = None

        ptr = half
        prev = None

        while ptr:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp

        # Merge List Logic
        half = prev

        while half and head:
            tail.next = head
            tail = tail.next
            head = head.next

            tail.next = half
            tail = tail.next
            half = half.next
        
        if head:
            tail.next = head
        if half:
            tail.next = half

        
