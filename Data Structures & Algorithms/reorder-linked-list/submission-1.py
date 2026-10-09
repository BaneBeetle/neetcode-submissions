# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Fast loop
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # When this ends, slow is pointed to the end of first half, slow.next is beginning of second half

        # Split the lists into two
        second = slow.next
        slow.next = None

        # Reverse the second half
        prev = None
        ptr = second

        while ptr:
            temp = ptr.next
            ptr.next = prev

            prev = ptr
            ptr = temp
        
        # Merge Two Sorted Lists

        dummy = ListNode()
        tail = dummy

        first = head
        second = prev

        while first and second:
            tail.next = first
            first = first.next
            tail = tail.next

            tail.next = second
            second = second.next
            tail = tail.next
        
        if first:
            tail.next = first
            first = first.next
            tail = tail.next
        if second:
            tail.next = second
            second = second.next
            tail = tail.next

