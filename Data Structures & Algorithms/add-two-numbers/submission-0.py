# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode()
        tail = dummy

        while l1 or l2 or carry:
            val1 = 0
            if l1:
                val1 = l1.val
            val2 = 0
            if l2:
                val2 = l2.val
            
            digit = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            print(digit)
            print(carry)

            tail.next = ListNode(digit)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
