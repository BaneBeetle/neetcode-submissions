# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head # .val .next

        # our goal is to make the last element our new head, change all their pointers

        before = None
        flag = True
        # x = y
        # if y changes, so does x
        if head is None or (head.next is None):
            return head

            
        while flag:

            # if we are at the beginning of the list
            if before is None:
                temp = current.next # remembers what our current neighbors are
                current.next = before
                before = current
                current = temp

   
            # if we are at the end of the list
            elif current.next is None:
                # this will run if we are at the last element
                current.next = before
                flag = False
                head = current


            # if we are at the middle (in betweens)
            else:
                temp = current.next
                current.next = before
                before = current
                current = temp
                
        return head


